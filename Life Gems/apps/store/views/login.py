from distutils.log import error
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import View


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'store/login.html')

    def post(self, request):
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    return redirect ('homepage')
            else:
                error_message = 'Invalid password'
        else:
            error_message = 'Please login to continue'

        print (email, password)
        context = {'error': error_message}
        return render (request, 'store/login.html', context)

def logout(request):
    request.session.clear()
    return redirect('login')