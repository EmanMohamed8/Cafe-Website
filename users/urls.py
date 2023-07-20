from django.urls import path, include
from .views import UserGetViews


urlpatterns = [ 
    path('users/<int:pk>/', UserGetViews.as_view())
]