from django.urls import path
from .views import index,contact,about

urlpatterns = [
    path('', index, name="home"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
]