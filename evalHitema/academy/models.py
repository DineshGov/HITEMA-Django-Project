from django.db import models

class Sport(models.Model):
    nomSport = models.CharField(
        max_length=100,
        unique=True,
        error_messages={'unique':"Un sport du même nom existe déjà!"}
        )
    """Unique ne gère pas la casse. Une erreur est ajoutée manuellement forms.py"""
    class Meta:
        verbose_name = "sport"
    
    def __str__(self):
        return self.nomSport