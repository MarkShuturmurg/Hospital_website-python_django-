from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name = 'MEDC-home'),
    path('profile/', views.profile, name = 'MEDC-profile'),
    path('appointment/', views.appointment, name = 'MEDC-appointment'),
    path('account/', views.account, name = 'MEDC-account'),
]