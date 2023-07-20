from django.urls import path, include
from .views import UserRegisterationViews, UserLoginViews
from knox import views as knox_views

urlpatterns = [
    path('Authentication/', include('knox.urls')),
    path('Authentication/register', UserRegisterationViews.as_view()),
    path('Authentication/login', UserLoginViews.as_view()),
    path('Authentication/logout',knox_views.LogoutView.as_view(), name="knox-logout"),
]