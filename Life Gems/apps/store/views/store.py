from django.shortcuts import render
from ..models.product import *
from ..models.orders import *
from .guestcheckout import *

# Create your views here.
def store(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)
