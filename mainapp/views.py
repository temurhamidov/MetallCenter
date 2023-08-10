from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.views import View
from .models import Contact, Product, ServiceBooking, ProductOrder
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView, TemplateView
from django.views.decorators.http import require_POST



class HomeView(View):
    def get(self, request):
        return render(request, 'mainapp/home.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        print(name)
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        service = request.POST.get('service')
        request = request.POST.get('request')
        ServiceBooking(name=name, phone=phone, date=date, service=service, request=request).save()
        return redirect('mainapp:home')


class AboutView(TemplateView):
    template_name = 'mainapp/about.html'


class ServiceView(View):
    def get(self, request):
        return render(request, 'mainapp/service.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        print(name)
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        service = request.POST.get('service')
        request = request.POST.get('request')
        ServiceBooking(name=name, phone=phone, date=date, service=service, request=request).save()
        return redirect('mainapp:service')


class BookingView(View):
    def get(self, request):
        return render(request, 'mainapp/booking.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        print(name)
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        service = request.POST.get('service')
        request = request.POST.get('request')
        ServiceBooking(name=name, phone=phone, date=date, service=service, request=request).save()
        return redirect('mainapp:booking')

class TeamView(TemplateView):
    template_name = 'mainapp/team.html'


class TestimonialView(TemplateView):
    template_name = 'mainapp/testimonial.html'


class CartView(TemplateView):
    template_name = 'mainapp/cart.html'


class ContactView(View):
    def get(self, request):
        return render(request, 'mainapp/contact.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contact(name=name, email=email, phone=phone, message=message).save()
        messages.success(request, "Information received. We will contact you soon.")
        return render(request, 'mainapp/contact.html')


class ProductView(TemplateView):
    template_name = 'mainapp/category.html'


class AllProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        paginator = Paginator(products, 5)
        current_page = request.GET.get('page')
        obj = paginator.get_page(current_page)
        nums = "a" * obj.paginator.num_pages

        context = {
            'products': obj,
            'nums': nums,
        }
        return render(request, 'mainapp/products.html', context)



class ProductListWithCategory(View):
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        products = Product.objects.filter(category__slug=slug)
        paginator = Paginator(products, 5)
        current_page = request.GET.get('page')
        obj = paginator.get_page(current_page)
        nums = "a" * obj.paginator.num_pages

        context = {
            'products': obj,
            'nums': nums,
        }
        return render(request, 'mainapp/products.html', context)


class ProductOrder(View):
    def get(self, request):
        return render(request, 'mainapp/ordering.html')

    def post(self, request):
        name = request.POST.get('name')
        telegram = request.POST.get('telegram')
        phone = request.POST.get('phone')
        aaa = ProductOrder(name=name, telegram=telegram, phone=phone)
        aaa.save()
        return redirect('mainapp:cart')






