from django.contrib import admin
from .models import Category, Product, Technicians, Contact, Service, ServiceBooking, ProductOrder


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'created']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'support_time']


@admin.register(Technicians)
class TechniciansAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'designation']



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'created']
    list_filter = ['created']
    search_fields = ['name']

@admin.register(ServiceBooking)
class ServiceBookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'service', 'created']
    list_filter = ['created']
    search_fields = ['name']


@admin.register(ProductOrder)
class ProductBookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'created']




