from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createuser, name='create-customers'),
    path('', views.getcustomers, name='customers-list'),
    path('delete/<int:id>', views.deletecustomers, name='customers-delete')
]