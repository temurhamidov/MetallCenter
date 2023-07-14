from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.views import View
from .models import Contact, Product
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView, TemplateView




class HomeView(TemplateView):
    template_name = 'mainapp/home.html'


class AboutView(TemplateView):
    template_name = 'mainapp/about.html'


class ServiceView(TemplateView):
    template_name = 'mainapp/service.html'


class BookingView(TemplateView):
    template_name = 'mainapp/booking.html'


class TeamView(TemplateView):
    template_name = 'mainapp/team.html'



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
    template_name = 'mainapp/product.html'


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




