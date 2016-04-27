from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response 
from django.views.generic import FormView
from django.views.generic import View
from forms import RegisterForm
from forms import ConnexionForm
from forms import Characterform
from forms import SyndicatForm
from forms import SelectSyndicatForm
from forms import SyndicatDashboardForm
from forms import SelectRoleForm
from forms import WorkPageForm
from forms import MarketForm
from forms import SellForm
from models import Character
from models import Syndicat
from models import Role
from models import Object
from numpy import int32
from datetime import datetime, timedelta
import time
from django.db import connection
from django.utils.timezone import utc
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
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
        user = request.user
        if user.is_authenticated() == True:
            return HttpResponseRedirect('/')
        if hasattr(user, 'character') == True:
            return HttpResponseRedirect('/')
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
        user = request.user
        if user.is_authenticated() == True:
            return HttpResponseRedirect('/')
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
        user = request.user
        if user.is_authenticated() == False:
            return HttpResponseRedirect('/')
        if hasattr(user, 'character') == True:
            return HttpResponseRedirect('/dashboard')
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
            food = Object(obj_type=1)
            food.character = character
            food.save()
            bandage = Object(obj_type=2)
            bandage.character = character
            bandage.save()
            return HttpResponseRedirect('/')
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)
            
class AddTimeView(View):
    template_name = 'templates/add_time.html'
    
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated() == False:
            return HttpResponseRedirect('/')
        if hasattr(user, 'character') == False:
            return HttpResponseRedirect('/')
        character = Character.objects.get(name=user.character.name)
        if character.role_bool == False:
            return HttpResponseRedirect('/dashboard')
        if user.character.d_pending.replace(tzinfo=None) > datetime.now().replace(tzinfo=None):
            return HttpResponseRedirect('/dashboard')
        role = Role.objects.get(name=user.character.role)
        character.role_exp = character.role_exp + character.pay
        stat1 = 0
        stat2 = 0
        if role.first_stat == "intelligence":
            stat1 = character.intelligence
            if character.role_exp >= 12:
                character.intelligence = character.intelligence + 2
        if role.first_stat == "stamina":
            stat1 = character.stamina
            if character.role_exp >= 12:
                character.stamina = character.stamina + 2
        if role.first_stat == "strength":
            stat1 = character.strength
            if character.role_exp >= 12:
                character.strength = character.strength + 2
        if role.first_stat == "observation":
            stat1 = character.observation
            if character.role_exp >= 12:
                character.observation = character.observation + 2
        if role.first_stat == "social":
            stat1 = character.social
            if character.role_exp >= 12:
                character.social = character.social + 2
        if role.second_stat == "intelligence":
            stat2 = character.intelligence
            if character.role_exp >= 12:
                character.intelligence = character.intelligence + 1
        if role.second_stat == "stamina":
            stat2 = character.stamina
            if character.role_exp >= 12:
                character.stamina = character.stamina + 1
        if role.second_stat == "strength":
            stat2 = character.strength
            if character.role_exp >= 12:
                character.strength = character.strength + 1
        if role.second_stat == "observation":
            stat2 = character.observation
            if character.role_exp >= 12:
                character.observation = character.observation + 1
        if role.second_stat == "social":
            stat2 = character.social
            if character.role_exp >= 12:
                character.social = character.social + 1
        if character.role_exp >= 12:
                character.role_exp = 0
        if character.role == "fermier":
            obj = Object.objects.get(character=character, obj_type=1)
            obj.count = obj.count + character.pay
            obj.save()
        character.pay = character.pay * role.pay + ((role.pay * 16 / 100) * stat1) + ((role.pay * 6 / 100) * stat2)
        character.time = character.time.replace(tzinfo=None) + timedelta(minutes = character.pay)
        character.role_bool = False
        character.save()
        return HttpResponseRedirect('/dashboard')

class DieView(View):
    template_name = 'templates/die.html'
    
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated() == False:
            return HttpResponseRedirect('/')
        if hasattr(user, 'character') == False:
            return HttpResponseRedirect('/')
        if user.character.state != "DEAD":
            return HttpResponseRedirect('/')
        character = Character.objects.get(name=user.character.name)
        character.delete()
        context = {}
        return render(request, self.template_name, context)

class DashboardView(View):
    template_name = 'templates/dashboard.html'
    
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated() == False:
            return HttpResponseRedirect('/')
        if hasattr(user, 'character') == False:
            return HttpResponseRedirect('/')
        character = Character.objects.get(name=user.character.name)
        if user.character.time.replace(tzinfo=None) > datetime.now().replace(tzinfo=None):
            time = user.character.time.replace(tzinfo=None) - datetime.now().replace(tzinfo=None)
            time = str(time.days) + " jours " + str(time.seconds//3600) + " heures " + str(time.seconds//60%60) + " minutes " + str(time.seconds%60) + " secondes "
        else:
            character.state = "DEAD"
            character.save()
            return HttpResponseRedirect('/die')
        if user.character.role_bool == True:
            if user.character.d_pending.replace(tzinfo=None) > datetime.now().replace(tzinfo=None):
                pending = user.character.d_pending.replace(tzinfo=None) - datetime.now().replace(tzinfo=None)
                pending = str(pending.seconds//3600) + " heures " + str(pending.seconds//60%60) + " minutes " + str(pending.seconds%60) + "     secondes "
            else:
                pending = "PAYDAY"
        else:
            pending = "Aucun"
        if (character.hungry.replace(tzinfo=None) - datetime.now().replace(tzinfo=None)) > timedelta(days=1):
            character.state = "Faim"
            character.save()
        nobjet = 0
        objet = Object.objects.all().filter(character=character)
        n = 0
        for n in objet:
            nobjet += n.count
        context = {}
        context["objet"] = nobjet
        context["role"] = user.character.role
        context["pending"] = pending
        context["time"] = time;
        context["stamina"] = user.character.stamina
        context["intelligence"] = user.character.intelligence
        context["strength"] = user.character.strength
        context["social"] = user.character.social
        context["observation"] = user.character.observation
        context["name"] = user.character.name
        context["syndicat"] = user.character.syndicat
        context["etat"] = user.character.state
        context["xp"] = 100 * user.character.role_exp / 12
        return render(request, self.template_name, context)
        
class CreateSyndicatView(FormView):
    template_name = 'templates/create_syndicat.html'
    form_class = SyndicatForm

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated() == False:
            return HttpResponseRedirect('/')
        if hasattr(user, 'character') == False:
            return HttpResponseRedirect('/')
        if user.character.syndicat != None or user.character.role != "Rien":
            return HttpResponseRedirect('/dashboard')
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
            syndicat = Syndicat(name=request.POST['name'], president=user.character)
            syndicat.save()
            character = Character.objects.get(name=user.character.name)
            character.syndicat = syndicat
            character.role = "President"
            character.save()
            return HttpResponseRedirect('/dashboard')
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)
            
class SelectSyndicatView(FormView):
    template_name = 'templates/select_syndicat.html'
    form_class = SelectSyndicatForm

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated() == False:
            return HttpResponseRedirect('/')
        if hasattr(user, 'character') == False:
            return HttpResponseRedirect('/')
        context = {}
        if user.character.syndicat != None:
            return HttpResponseRedirect('/dashboard')
        context["syndicat"] = Syndicat.objects.all()
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            user = request.user
            syndicat = Syndicat.objects.get(name=request.POST['name'])
            character = Character.objects.get(name=user.character.name)
            character.syndicat = syndicat
            syndicat.membres = syndicat.membres + 1
            character.save()
            syndicat.save()
            return HttpResponseRedirect('/dashboard')
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)
            
class SyndicatDashboardView(FormView):
    template_name = 'templates/dashboard_syndicat.html'
    form_class = SyndicatDashboardForm

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated() == False:
            return HttpResponseRedirect('/')
        if hasattr(user, 'character') == False:
            return HttpResponseRedirect('/')
        syndicat = Syndicat.objects.get(name=user.character.syndicat)
        if user.character.syndicat == None:
            return HttpResponseRedirect('/dashboard')
        if syndicat.banque.replace(tzinfo=None) > datetime.now().replace(tzinfo=None):
            time = syndicat.banque.replace(tzinfo=None) - datetime.now().replace(tzinfo=None)
            time = str(time.days) + " jours " + str(time.seconds//3600) + " heures " + str(time.seconds//60%60) + " minutes " + str(time.seconds%60) + " secondes "
        else:
            time = str(0) + " jours " + str(0) + " heures " + str(0) + " minutes " + str(0) + " secondes "
        context = {}
        context['syndicat'] = syndicat
        context['time'] = time
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            user = request.user
            syndicat = Syndicat.objects.get(name=request.POST['name'])
            character = Character.objects.get(name=user.character.name)
            character.syndicat = None
            syndicat.membres = syndicat.membres - 1
            character.save()
            syndicat.save()
            return HttpResponseRedirect('/dashboard')
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)
            
class WorkPageView(FormView):
    template_name = 'templates/workpage.html'
    form_class = WorkPageForm
    
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated() == False:
            return HttpResponseRedirect('/')
        if hasattr(user, 'character') == False:
            return HttpResponseRedirect('/')
        context = {}
        if user.character.state != "Aucun":
            return HttpResponseRedirect('/dashboard')
        if user.character.role == "Rien":
            return HttpResponseRedirect('/dashboard')
        if user.character.role == "President":
            return HttpResponseRedirect('/dashboard_syndicat')
        context["character"] = user.character
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            user = request.user
            role = Role.objects.get(name=user.character.role)
            character = Character.objects.get(name=user.character.name)
            if int(request.POST['hour']) == -2:
                character.role_bool = False
                character.role = "Rien"
                character.role_exp = 0
                character.save()
                return HttpResponseRedirect('/dashboard')
            if character.role_bool == True:
                character.role_bool = False
                character.save()
                return HttpResponseRedirect('/dashboard')
            character.role_bool = True
            time = int(request.POST['hour'])
            character.d_pending = datetime.now().replace(tzinfo=None) + timedelta(hours = time)
            character.pay = time
            character.save()
            return HttpResponseRedirect('/dashboard')
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

class SelectRoleView(FormView):
    template_name = 'templates/select_role.html'
    form_class = SelectRoleForm

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated() == False:
            return HttpResponseRedirect('/')
        context = {}
        if hasattr(user, 'character') == False:
            return HttpResponseRedirect('/')
        if user.character.state != "Aucun":
            return HttpResponseRedirect('/dashboard')
        if user.character.role != "Rien":
            return HttpResponseRedirect('/workpage')
        context["stat_role"] = ["stamina", "intelligence", "strength", "social", "observation"]
        context["stat_chara"] = [("stamina", user.character.stamina), ("intelligence", user.character.intelligence), ("strength", user.character.strength), ("social", user.character.social), ("observation", user.character.observation)]
        context["role"] = Role.objects.all()
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            user = request.user
            role = Role.objects.get(name=request.POST['name'])
            character = Character.objects.get(name=user.character.name)
            character.role = role.name
            character.save()
            return HttpResponseRedirect('/dashboard')
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)
            
class MarketView(FormView):
    template_name = 'templates/market.html'
    form_class = MarketForm
    
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated() == False:
            return HttpResponseRedirect('/')
        if hasattr(user, 'character') == False:
            return HttpResponseRedirect('/')
        if user.character.state != "Aucun":
            return HttpResponseRedirect('/dashboard')
        context = {}
        context['objet'] = Object.objects.all().exclude(quantity_sell=0)
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            user = request.user
            character = Character.objects.get(name=user.character.name)
            obj_seller = Object.objects.get(id=int(request.POST['obj']))
            obj_buyer = Object.objects.get(character=character, obj_type=obj_seller.obj_type)
            seller = Character.objects.get(name=obj_seller.character.name)
            obj_seller.quantity_sell = obj_seller.quantity_sell - int(request.POST['nb'])
            obj_buyer.count = obj_buyer.count + int(request.POST['nb'])
            price = int(request.POST['nb']) * obj_seller.price
            if seller.syndicat != None:
                syndicat = Syndicat.objects.get(name=seller.syndicat.name)
                percent = price * 25 / 100
                price = price - percent
                if syndicat.banque.replace(tzinfo=None) > datetime.now().replace(tzinfo=None):
                    syndicat.banque = syndicat.banque.replace(tzinfo=None) + timedelta(minutes=percent)
                else:
                    syndicat.banque = datetime.now().replace(tzinfo=None) + timedelta(minutes=percent)
                syndicat.save()
            character.time = character.time.replace(tzinfo=None) - timedelta(minutes=price)
            character.save()
            seller.time = seller.time.replace(tzinfo=None) + timedelta(minutes=price)
            seller.save()
            obj_buyer.save()
            obj_seller.save()
            return HttpResponseRedirect('/dashboard')
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)
            
class SellView(FormView):
    template_name = 'templates/market_sell.html'
    form_class = SellForm
    
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated() == False:
            return HttpResponseRedirect('/')
        if hasattr(user, 'character') == False:
            return HttpResponseRedirect('/')
        if user.character.state != "Aucun":
            return HttpResponseRedirect('/dashboard')
        objet = Object.objects.all().filter(character=user.character)
        context = {}
        context['sell_objet'] = objet.exclude(count=0)
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            user = request.user
            character = Character.objects.get(name=user.character.name)
            obj = Object.objects.get(character=character,obj_type=int(request.POST['obj']))
            obj.count = obj.count - int(request.POST['nb'])
            obj.quantity_sell = obj.quantity_sell + int(request.POST['nb'])
            obj.price = int(request.POST['price'])
            obj.save()
            return HttpResponseRedirect('/dashboard')
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)
            
class InventoryView(View):
    template_name = 'templates/inventory.html'
    
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated() == False:
            return HttpResponseRedirect('/')
        if hasattr(user, 'character') == False:
            return HttpResponseRedirect('/')
            return HttpResponseRedirect('/dashboard')
        objet = Object.objects.all().filter(character=user.character)
        context = {}
        context['objet'] = objet.exclude(count=0)
        return render(request, self.template_name, context)