from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('sports', views.show_sports, name='sports'),
    path('create/sport', views.create_sport, name='create_sport'),
    path('update/sport/<int:id_sport>', views.update_sport, name='update_sport'),
    path('delete/sport/<int:id_sport>', views.delete_sport, name='delete_sport'),
    path('equipes', views.show_equipes, name='equipes'),
    path('create/equipe', views.create_equipe, name='create_equipe'),
    path('update/equipe/<int:id_equipe>', views.update_equipe, name='update_equipe'),
]
