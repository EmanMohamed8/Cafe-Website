from django.urls import path
from . import views

urlpatterns = [
    path('home/home.html', views.home),
    path('registration/login.html', views.login),
    path('about/about.html', views.about),
    path('service/service.html', views.service),
    path('contact/contact.html', views.contact),
    path('gallery/gallery.html', views.gallery),
]
