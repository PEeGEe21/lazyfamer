from django.shortcuts import redirect, render

from .forms import NewUserForm
from home.models import *
from home.filters import *
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View


# Create your views here.
def register(request):
    userForm = NewUserForm()
    mydict={'userForm': userForm}
    if request.method == 'POST':
        userForm=NewUserForm(request.POST)
        if userForm.is_valid():
            user=userForm.save()
            user.save()
        return redirect('login')
    return render (request, 'users/signup.html', context=mydict)


def dashboard(request):
    user = request.user
    print(user)
    orders = Order.get_orders_by_user(user)
    print(orders)
    context = {
        'orders': orders,
    }
    return render(request, 'users/dashboard.html', context)


def services(request):
        services = Service.objects.all()
        categories = Category.objects.all()
        print(services);
        myFilter = CategoryFilter(request.GET, queryset=categories)
        categories = myFilter.qs
        
        context = {
            'services': services,
            'categories': categories,
            'myFilter': myFilter
        }
        return render(request, 'users/services.html', context)




  
  
# class OrderView(View):

#     def get(self, request):
#         user = request.user
#         print(user)
#         orders = Order.get_orders_by_user(user)
#         print(orders)
#         return render(request, 'users/dashboard.html', {'orders': orders})