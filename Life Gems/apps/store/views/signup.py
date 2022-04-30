from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('first name')
        last_name = postData.get('last name')
        email = postData.get('email')
        password = postData.get('password')
        phone_no = postData.get('phone number')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone_no
        }
        error_message = None

        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone_no=phone_no
        )
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, email, password, phone_no)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        # Check first name
        if not customer.first_name:
            error_message = 'First name is required.'
        elif len(customer.first_name) < 3:
            error_message = 'First name must be greater than 3 characters.'
        elif len(customer.first_name) > 50:
            error_message = 'First name must be less than 50 characters.'
        # Check last name
        elif not customer.last_name:
            error_message = 'Last name is required.'
        elif len(customer.last_name) < 3:
            error_message = 'Last name must be greater than 3 characters.'
        elif len(customer.last_name) > 50:
            error_message = 'Last name must be less than 50 characters.'
        # Check email
        elif not customer.email:
            error_message = 'Email is required.'
        elif len(customer.email) < 5:
            error_message = 'Email must be greater than 5 characters.'
        elif customer.emailExists():
            error_message = 'This email address is already in use.'
        # Check password
        elif len(customer.password) < 5:
            error_message = 'Password must be greater than 5 characters.'
        # Check phone number
        elif not customer.phone_no:
            error_message = 'Phone number is required.'
        elif len(customer.phone_no) < 9:
            error_message = 'Phone number must be at least 9 numbers characters long.'

        return error_message
