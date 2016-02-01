from django import forms
from django.db import models
from django.contrib.auth.models import User
from models import Character
from django.contrib.auth import authenticate, login, logout

class RegisterForm(forms.Form):
    pseudo = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length=50)
    confpass = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        pseudo = cleaned_data.get("pseudo")
        password = cleaned_data.get("password")
        email = cleaned_data.get("email")
        confpass = cleaned_data.get("confpass")
        if User.objects.filter(username=pseudo).exists():
            raise forms.ValidationError("Le pseudo existe deja nique ta mere")
        if len(pseudo) < 5:
            raise forms.ValidationError("La longueur de votre pseudo doit etre comprise entre 3 et 15 caracteres")
        if len(password) < 5:
            raise forms.ValidationError("La longueur de votre mot de passe doit etre comprise entre 8 et 32 caracteres")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("L'email existe deja")
        if password != confpass:
            raise forms.ValidationError("Mot de passe differrent")
        return cleaned_data

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
    MY_CHOICES = (
        ('male', 'Homme'),
        ('female', 'Femme'),
    )
    gender = forms.ChoiceField(label="Gender", widget=forms.RadioSelect, choices=MY_CHOICES)
    name = forms.CharField(max_length=20)
    
    def __init__(self, *args, **kwargs):
        super(Characterform, self).__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs['class'] = 'with-gap'
    
    def clean_name(self):
        data = self.cleaned_data['name']
        if Character.objects.filter(name=data).exists() == True:
            raise forms.ValidationError("Le pseudo exists")
        return data
        
    def gender_choices(self):
        field = self['gender']
        widget = field.field.widget

        attrs = {}
        auto_id = field.auto_id
        if auto_id and 'id' not in widget.attrs:
            attrs['id'] = auto_id

        name = field.html_name

        return widget.get_renderer(name, field.value(), attrs=attrs)