from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
  class Meta:
    model = Reservation
    fields = ['name', 'email', 'phone_number', 'date', 'time', 'number_of_guests', 'occasion', 'agreed_to_terms']
    


