"""
URL configuration for inventory_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('login/', views.userlogin, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('product-list', views.productList, name='product-list'),
    path('product-add', views.productadd, name='product-add'),
    path('product-grid', views.productgrid, name='product-grid'),
    path('product-detail', views.productdetails, name='product-detail'),
    path('product-edit', views.productedit, name='product-edit'),
    path('categories-edit', views.categoriesedit, name='categories-edit'),
    path('categories-list', views.categorieslist, name='categories-list'),
    path('categories-add', views.categoriesadd, name='categories-add'),
    # orders
    path('order-details', views.ordersdetails, name='order-details'),
    path('order-list', views.orderslist, name='order-list'),
    path('order-invoices', views.orderinvoices, name='order-invoices'),

    # customers

    path('customers-list', views.customerlist, name='customers-list'),
    path('customers-details', views.customersdetails, name='customers-details'),


    # customers app
    path('user/', include('user.urls')),
]
