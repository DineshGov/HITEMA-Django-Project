from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('sports', views.read_sports, name='sports'),
    path('create/sport', views.create_sport, name='create_sport'),
    path('update/sport/<int:id_sport>', views.update_sport, name='update_sport'),
]
