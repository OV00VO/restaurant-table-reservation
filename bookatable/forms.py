# Reference in modified parts below: Code Institute Curriculum and Code Star Project   
# Reference in modified parts below: https://github.com/flatplanet/Django-CRM
# Notes: Below code is based on the above references and modifed for the project

from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
  class Meta:
    model = Reservation
    fields = ['name', 'email', 'phone_number', 'date', 'time', 'number_of_guests', 'occasion', 'agreed_to_terms']
    


