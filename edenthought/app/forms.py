from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Thought


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=63)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
    

class ThoughtForm(forms.ModelForm):
    
    class Meta:
        model = Thought
        fields = ["title", "content"]
        exclude = ["user"]
        
    