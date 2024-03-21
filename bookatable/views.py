from django.shortcuts import render, redirect
#from django.http import generic
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def menu(request):
    context = {}
    return render(request, 'menu.html', context)

def reservations(request):
    context = {}
    return render(request, 'reservations.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def bookings(request):
    context = {}
    return render(request, 'bookings.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)

def logout(request):
    context = {}
    return render(request, 'logout.html', context)

def logout_confirm(request):
    context = {}
    return render(request, 'logout_confirm.html', context)

def record(request):
    context = {}
    return render(request, 'record.html', context)

def login_form(request):
    context = {}
    return render(request, 'login_form.html', context)

def add_record(request):
    context = {}
    return render(request, 'add_record.html', context)

def register(request):
    context = {}
    return render(request, 'register.html', context)

def terms(request):
    context = {}
    return render(request, 'terms.html', context)

def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')  # Redirect to your desired page after login
