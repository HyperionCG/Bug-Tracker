from django import forms
from bug_app.models import Ticket
from django.utils import timezone

class TicketForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=200)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=50)