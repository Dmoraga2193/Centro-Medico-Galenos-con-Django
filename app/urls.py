from django.urls import path
from .views import index,contact,about,registro

urlpatterns = [
    path('', index, name="home"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('registro/',registro,name="registro"),
]