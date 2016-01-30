from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class RegisterForm(forms.Form):
    pseudo = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length=50)
    
    def clean_pseudo(self):
        data = self.cleaned_data['pseudo']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError("Le pseudo existe deja nique ta mere")
        if len(data) < 5:
            raise forms.ValidationError("La longueur de votre pseudo doit etre comprise entre 3 et 15 caracteres")
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        if len(data) < 5:
            raise forms.ValidationError("La longueur de votre mot de passe doit etre comprise entre 8 et 32 caracteres")
        return data
        
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("L'email existe deja")
        return data
        
class ConnexionForm(forms.Form):
    pseudo = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean_pseudo(self):
        data = self.cleaned_data['pseudo']
        if User.objects.filter(username=data).exists() == False:
            raise forms.ValidationError("Le pseudo n'exists pas")
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        return data
        
class Characterform(forms.Form):
    name = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=10)
    
    def clean_name(self):
        data = self.cleaned_data['name']
        if User.objects.filter(name=data).exists():
            raise forms.ValidationError("Le nom existe deja")
        if len(data) < 5:
            raise forms.ValidationError("La longueur de votre nom doit etre comprise entre 3 et 15 caracteres")
        return data