from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.otp_register, name='register'),
    path('login/', views.otp_login, name='login'),
    path('verify/', views.otp_verify, name='verify'),
    path('status/', views.otp_status, name='status'),
    path('logout/', views.otp_logout, name='logout'),
    path('token/', views.otp_token, name='token'),
]
