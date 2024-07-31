from django.urls import path
from .views import register, login, protected_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('protected/', protected_view, name='protected'),
]
