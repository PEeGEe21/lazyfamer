from django.contrib import admin
from .models import Category, Service, Order

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Category)

# admin.site.register(Exam)
admin.site.site_header = 'LazyFamer'
admin.site.site_title = 'LazyFamer'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # What information to display
    list_display = ('title', 'rate', 'min_order', 'max_order', 'category','slug', 'draft', 'publish')
    list_filter = ("rate", "category", "draft")
    search_fields = ['title', 'rate', 'category']
    list_display_links = ('title', 'rate')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # What information to display
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # What information to display
    list_display = ('user', 'service', 'price', 'date', 'status')
