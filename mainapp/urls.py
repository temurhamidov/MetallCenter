from django.urls import path
from .views import HomeView, AboutView, ContactView, TeamView, ProductView, ProductListWithCategory, ServiceView, BookingView, AllProductsView, TestimonialView
from .views import CartView, ProductOrder
app_name = 'mainapp'
urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('service/', ServiceView.as_view(), name='service'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
    path('team/', TeamView.as_view(), name='team'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('product/', ProductView.as_view(), name='product'),
    path('all-products/', AllProductsView.as_view(), name='all-products'),
    path('cart/', CartView.as_view(), name='cart'),
    path('product-order/', ProductOrder.as_view(), name='product-order'),
    path('products/<slug:slug>', ProductListWithCategory.as_view(), name='products_category'),

]