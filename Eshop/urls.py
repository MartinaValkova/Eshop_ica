"""Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shop import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='shop/logout.html'), name='logout'),
    path('contact/', views.contact, name='contact'),
    path('terms/', auth_views.LogoutView.as_view(template_name='shop/terms.html'), name='terms'),
    path('privacy/', auth_views.LogoutView.as_view(template_name='shop/privacy.html'), name='privacy'),
    path('sales/', auth_views.LogoutView.as_view(template_name='shop/sales.html'), name='sales'),
    path('accountLocked/', views.accountLocked, name= 'accountLocked'),

]


