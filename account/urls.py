from django.shortcuts import path

from account import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('/signup/', views.signup, name='signup')
]