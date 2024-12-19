from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('equipment_booking/', views.equipment_booking, name='equipment_booking'),
    path('booking_history/', views.booking_history, name='booking_history'),
    path('equipment_management/', views.equipment_management, name='equipment_management'),
    path('login/', views.login_view, name='login'),
]
