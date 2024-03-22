from django.db import models 
from django.shortcuts import render, redirect
from django import forms

class Reservation(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  phone = models.CharField(max_length=20)
  date = models.DateField()
  time = models.TimeField()
  guests = models.PositiveIntegerField()
  occasion = models.TextField(blank=True)
  agree_to_terms = models.BooleanField()

  def __str__(self):
    return f"{self.name} - {self.date} ({self.time})"

class ReservationForm(forms.ModelForm):
  class Meta:
    model = Reservation
    fields = ['name', 'email', 'phone', 'date', 'time', 'guests', 'occasion', 'agree_to_terms']

def create_reservation(request):
  if request.method == 'POST':

    if form.is_valid():
      reservation = form.save(commit=False)
      reservation.save()
      return redirect('reservation_success')
    else:
      pass
  else:
    form = ReservationForm()

  return render(request, 'reservation_form.html', {'form': form})
  
class TestModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

def __str__(self):
    return self.name

from django.db import models

class Item(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True)

  def __str__(self):
    return self.name
   