# frontend/urls.py
from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('sugerencias/', views.sugerencia_view, name='sugerencias'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('carrito/', views.carrito, name='carrito'),
    path('pago/', views.pago, name='pago'),
    path('signup/', views.signup, name='signup'),
    path('navbar/', views.navbar, name='navbar'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
]
