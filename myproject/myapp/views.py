from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def equipment_booking(request):
    return render(request, 'myapp/equipment_booking.html')

def booking_history(request):
    return render(request, 'myapp/booking_history.html')

def equipment_management(request):
    return render(request, 'myapp/equipment_management.html')

def login_view(request):
    return render(request, 'myapp/login.html')
