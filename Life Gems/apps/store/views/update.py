from django.http import JsonResponse
from django.views import View
from store.models.product import *
from store.models.orders import *
import json

class updateItem(View):
  def post(self, request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    print('Action:', action)
    print('productID:', productID)
    
    customer = request.user.customer
    product = Product.objects.get(id=productID)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
      orderItem.quantity += 1
    elif action == 'remove':
      orderItem.quantity -= 1
      
    orderItem.save()
    
    if orderItem.quantity <= 0:
      orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)