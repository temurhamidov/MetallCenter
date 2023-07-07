from django.urls import path
from .views import HomeView, AboutView, ContactView, TeamView, TestimonialView, ProductView, ServiceView, BookingView

app_name = 'mainapp'
urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('service/', ServiceView.as_view(), name='service'),
    path('contact', ContactView.as_view(), name='contact'),
    path('team/', TeamView.as_view(), name='team'),
    path('testimonial', TestimonialView.as_view(), name='testimonial'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('product/', ProductView.as_view(), name='product'),

]