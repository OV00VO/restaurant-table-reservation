from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from allauth.account.views import LoginView
from .models import TestModel
from .models import Item

def index(request):
    context = {}
    return render(request, 'index.html', context)

def menu(request):
    context = {}
    return render(request, 'menu.html', context)

def reservations(request):
    context = {}
    return render(request, 'reservations.html', context)

def reservation_success(request):
    context = {}
    return render(request, 'reservation_success.html', context)

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
pass

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
      return redirect('home')

def create_reservation(request):
    reservation = form.save()
    context = {'reservation': reservation}
    return render(request, 'reservation_success.html', context)

def test_crud(request):
  if request.method == 'POST':
    form = TestModelForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('test_crud')

  entries = TestModel.objects.all()
  form = TestModelForm()
  context = {'entries': entries, 'form': form}
  return render(request, 'test_crud.html', context)

def crud_page(request):
  if request.method == 'POST':
    form = ItemForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('crud_page')

  entries = ItemForm.objects.all()
  form = ItemForm()
  context = {'entries': entries, 'form': form}
  return render(request, 'crud_page.html', context)
