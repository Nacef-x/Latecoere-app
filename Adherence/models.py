from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Material(models.Model):
    centre_profit = models.IntegerField()
    article_code = models.CharField(max_length=100)
    division = models.IntegerField()
    gestionnaire = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    planning = models.CharField(max_length=100)
    commentaire = models.TextField(max_length=1000)
    cycle_appro = models.IntegerField()
    cycle_manuf= models.IntegerField()
    cle_horizon = models.IntegerField()
    delai_securite = models.IntegerField()
    temps_reception = models.IntegerField()
    cle = models.IntegerField()

class Division(models.Model):
    Name= models.CharField(max_length=100)
    Site= models.CharField(max_length=100)


class Zpp(models.Model):
    article = models.CharField(max_length=100)
    date_dispo = models.DateField(auto_now_add=False,auto_now=True)
    element = models.CharField(max_length=100)
    ordre = IntegerField()
    message = IntegerField()
    date_reordo = IntegerField()
    division = models.ForeignKey(Division,on_delete=models.CASCADE)