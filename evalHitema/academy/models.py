from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Sport(models.Model):
    nomSport = models.CharField(
        max_length = 100,
        unique = True,
        error_messages = {'unique':"Un sport du même nom existe déjà!"}
        )
    """Unique ne gère pas la casse. Une erreur est ajoutée manuellement forms.py"""
    class Meta:
        verbose_name = "sport"
    
    def __str__(self):
        return self.nomSport

class Equipe(models.Model):
    nomEquipe = models.CharField(
        max_length = 100,
        unique = True,
        )
    sport = models.ForeignKey(
        'Sport',
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
        )
    joueurs = models.ManyToManyField(
        'Joueur',
        blank=True,
        )

    class Meta:
        verbose_name = "equipe"
    
    def __str__(self):
        return self.nomEquipe

class Joueur(models.Model):
    nomJoueur = models.CharField(
        max_length = 100,
        unique = True,
        )
    equipes = models.ManyToManyField(
        'Equipe',
        through=Equipe.joueurs.through,
        blank=True)
    class Meta:
        verbose_name = "joueur"
    
    def __str__(self):
        return self.nomJoueur