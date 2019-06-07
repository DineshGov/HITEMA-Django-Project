from django.db import models

class Sport(models.Model):
    nomSport = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "sport"
    
    def __str__(self):
        return self.nomSport