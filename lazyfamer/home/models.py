from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
import datetime
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, null=True)

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('category')
    def get_absolute_url(self):
        return self.slug

# choices = [item for item in Category.objects.all().values_list('name', 'name')]


class Service(models.Model):
    title = models.CharField(max_length=500)
    rate = models.DecimalField(decimal_places=2, max_digits=500)
    min_order = models.BigIntegerField()
    max_order = models.BigIntegerField()
    description = RichTextField(default='', null=True, blank="True")
    # category = models.CharField(choices=choices, max_length=255, null=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE, related_name='services')
    slug = models.SlugField(unique=True)
    draft = models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now_add=True)


    objects = models.Manager()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('service-detail', kwargs={'slug': self.pk})
    def get_absolute_url(self):
        return self.slug

  
  
class Order(models.Model):
    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                                 on_delete=models.CASCADE)
    # total_rate = models.IntegerField(default=1)
    quantity = models.IntegerField(default=1)

    price = models.IntegerField()
    # address = models.CharField(max_length=50, default='', blank=True)
    # phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
  
    def placeOrder(self):
        self.save()
  
    @staticmethod
    def get_orders_by_user(user_id):
        return Order.objects.filter(user=user_id).order_by('-date')
