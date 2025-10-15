from django.urls import path
from . import views

app_name = 'address_book'

urlpatterns = [
    path('', views.add_address, name='home'),           # ✅ new: makes "/" work
    path('add_address/', views.add_address, name='add_address'),
]
