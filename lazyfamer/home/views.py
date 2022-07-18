from unicodedata import category
from django.shortcuts import render
from .models import Service, Category
from .filters import ServiceFilter, CategoryFilter
# Create your views here.
def index(request):
        return render(request, 'home/index.html')

def aboutUs(request):
        return render(request, 'home/about-us.html')

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
        return render(request, 'home/services.html', context)



        

    


