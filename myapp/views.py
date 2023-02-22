from django.shortcuts import render

# Create your views here.


def home(requset):
    return render(requset, 'project/home/home.html')
def login(requset):
    return render(requset, 'registration/login.html')
def about(requset):
    return render(requset, 'project/about/about.html')
def service(requset):
    return render(requset, 'project/service/service.html')
def contact(requset):
    return render(requset, 'project/contact/contact.html')
def gallery(requset):
    return render(requset, 'project/gallery/gallery.html')