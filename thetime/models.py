from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Territory(models.Model):
    name = models.CharField(max_length=50)
    ressource_type = models.CharField(max_length=50)
    stock = models.IntegerField(default=1000)
    factory = models.BooleanField(default=False)
    level_factory = models.IntegerField(default=0)
    
    owner = models.OneToOneField('Syndicat', on_delete=models.CASCADE, related_name="territory")
    
    def __str__(self):
        return self.name

class Syndicat(models.Model):
    name = models.CharField(max_length=50)
    banque = models.IntegerField(default=0)
    niveau = models.IntegerField(default=1)
    membres = models.IntegerField(default=1)
    president = models.OneToOneField('Character', on_delete=models.CASCADE, related_name="syndicat_president")
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Syndicat, self).save(*args, **kwargs)

class Character(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    time = models.DateTimeField(default=datetime.now()+timedelta(days=7))
    pa = models.IntegerField(default=0)
    role = models.CharField(max_length=50, default="Rien")
    pending = models.CharField(max_length=50, default="Rien")
    d_pending = models.DateTimeField(default=datetime.now())
    
    # Stats
    stamina = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    social = models.IntegerField(default=0)
    observation = models.IntegerField(default=0)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    syndicat = models.ForeignKey(Syndicat, on_delete=models.CASCADE, related_name="character", null=True, blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Character, self).save(*args, **kwargs)

# Create your models here.


