from django.urls import path
from . import views

urlpatterns = [
    path('create-customers', views.createuser, name='create-customers'),
    path('customers-list', views.getcustomers, name='customers-list'),
]