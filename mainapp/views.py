from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
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


class TestimonialView(TemplateView):
    template_name = 'mainapp/testimonial.html'


class ContactView(TemplateView):
    template_name = 'mainapp/contact.html'


class ProductView(TemplateView):
    template_name = 'mainapp/product.html'

