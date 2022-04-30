from django.shortcuts import render
from django.views import View
from store.models.product import Product
from ..models.customer import Customer
from .guestcheckout import *

def cart(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)
