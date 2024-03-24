from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  email = models.EmailField()
  phone_number = models.CharField(max_length=20)
  date = models.DateField()
  time = models.TimeField()
  number_of_guests = models.PositiveIntegerField()
  occasion = models.TextField(blank=True)
  agreed_to_terms = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.name} - {self.date} ({self.time})"