import django_filters
from django_filters import ModelChoiceFilter, CharFilter

from .models import *

class ServiceFilter(django_filters.FilterSet):
    class Meta:
        model = Service
        fields= ('title','rate', 'min_order', 'max_order', 'category')

class CategoryFilter(django_filters.FilterSet):
    name = ModelChoiceFilter(queryset=Category.objects.all())
    services = CharFilter(field_name='services', lookup_expr='title__icontains')
    class Meta:
        model = Category
        fields= '__all__'
        exclude = ['slug']
