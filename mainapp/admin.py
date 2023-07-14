from django.contrib import admin
from .models import Category, Product, Technicians, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'created']


@admin.register(Technicians)
class TechniciansAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'designation']



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'created']
    list_filter = ['created']
    search_fields = ['name']


