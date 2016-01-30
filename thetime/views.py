from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import FormView
from django.views.generic import View
from forms import RegisterForm
from forms import ConnexionForm
from forms import Characterform
from models import Character
import time
from django.db import connection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class Home(View):
    template_name = 'templates/home.html'

    def get(self, request, *args, **kwargs):
        guigui = {}
        guigui["couscous"] = "choumouche"
        guigui["mawtin"] = "dehdzhdhede"
        return render(request, self.template_name, guigui)
        
class RegisterView(FormView):
    template_name = 'templates/register.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            user = User.objects.create_user(username=request.POST['pseudo'],
                                            email=request.POST['email'],
                                            password=request.POST['password'])
            return HttpResponseRedirect('/')
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

class ConnexionView(FormView):
    template_name = 'templates/connexion.html'
    form_class = ConnexionForm

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        error = False
        context = self.get_context_data(**kwargs)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            username = request.POST.get('pseudo', False)
            password = request.POST.get('password', False)
            user = authenticate(username=username, password=password)
            if user is not None:
                 # the password verified for the user
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/create_character')
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
            return render(request, self.template_name, context)
            
        else:
            return self.form_invalid(form, **kwargs)

class DeconnexionView(View):
    template_name = 'templates/deconnexion.html'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
        
class CharacterCreateView(FormView):
    template_name = 'templates/create_character.html'
    form_class = Characterform

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            user = request.user
            character = Character(user=user, name=request.POST['name'], gender=request.POST['gender'])
            character.save()
            return HttpResponseRedirect('/')
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)