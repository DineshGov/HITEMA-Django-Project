from django.db import models

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
        error_messages = {
            'unique':"Une équipe du même nom existe déjà!",
            'max_length':"Veuillez choisir un nom plus court."
        }
        )
    sport = models.ForeignKey(
        'Sport',
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
        )
    class Meta:
        verbose_name = "equipe"
    
    def __str__(self):
        return self.nomEquipe