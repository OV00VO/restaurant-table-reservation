
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms

from .models import Record
from .models import TestModel
from .models import Item
from .models import Reservation


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address'
    }))
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        }))
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        }))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = """
Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
"""

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        password_help_text = """
<ul class="form-text text-muted small">
  <li>Your password can't be too similar to other personal information.</li>
  <li>Your password must contain at least 8 characters.</li>
  <li>Your password can't be a commonly used password.</li>
  <li>Your password can't be entirely numeric.</li>
</ul>
"""


self.fields['password1'].help_text = password_help_text
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2']
        .widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        spassword_confirm_help_text = """
<span class="form-text text-muted small">
  Enter the same password as before, for verification.
</span>
"""

self.fields['password2'].help_text = password_confirm_help_text


class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super(AddRecordForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                "placeholder": field.label.lower(),
                "class": "form-control",
            }
            self.fields[field].required = True


class TestModelForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ['name', 'description']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']


class ReservationForm(forms.ModelForm):


class Meta:
    model = Reservation
    fields = (
        'name',
        'email',
        'phone_number',
        'date',
        'time',
        'number_of_guests',
        'occasion',
        'agreed_to_terms',
    )
