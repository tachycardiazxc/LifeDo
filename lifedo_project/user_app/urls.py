from django.urls import path
from .views import UserCreationView, UserAuthenticationView, UserLogoutView \

urlpatterns = [
    path('register/', UserCreationView.as_view(), name='register'),
    path('login/', UserAuthenticationView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout')
]
