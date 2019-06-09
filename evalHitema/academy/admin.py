from django.contrib import admin
from .models import *

admin.site.register(Sport)
admin.site.register(Equipe, MyModelAdmin)
admin.site.register(Joueur, MyModelAdmin)
