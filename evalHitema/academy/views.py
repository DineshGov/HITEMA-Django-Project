from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from academy.models import *
from .forms import *

def root(request):
    """ redirige http://127.0.0.1:8000 vers http://127.0.0.1:8000/academy/ """
    return redirect(accueil)

def accueil(request):
    """ page d'accueil: http://127.0.0.1:8000/academy/ """
    return render(request, 'academy/home.html')




def show_sports(request):
    sports = Sport.objects.all()
    return render(request, 'academy/sports.html', {'sports':sports})

def create_sport(request):
    form = SportForm(request.POST or None)

    if form.is_valid(): 
        nomSport = form.cleaned_data['nomSport']
        form.save()
        return redirect('sports')
    return render(request, 'academy/createSport.html', locals())

def read_sport(request, id_sport):
    sport = get_object_or_404(Sport, id=id_sport)
    equipes = Equipe.objects.filter(sport = Sport.objects.get(id=id_sport))
    return render(request, 'academy/readSport.html', locals())

def update_sport(request, id_sport):
    sport = get_object_or_404(Sport, id=id_sport)
    form = SportForm(request.POST or None, instance=sport)
    if form.is_valid():
        form.save()
        envoi = True
    return render(request, "academy/updateSport.html", locals())

def delete_sport(request, id_sport):
    sport = get_object_or_404(Sport, id=id_sport)
    if sport:
        nom = sport.nomSport
        sport.delete()
        suppression = True
    return render(request, 'academy/deleteSport.html', locals())




def show_equipes(request):
    equipes = Equipe.objects.all()
    return render(request, 'academy/equipes.html', {'equipes':equipes})

def create_equipe(request):
    form = EquipeForm(request.POST or None)
    if form.is_valid(): 
        nomEquipe = form.cleaned_data['nomEquipe']
        form.save()
        return redirect('equipes')
    return render(request, 'academy/createEquipe.html', locals())

def read_equipe(request, id_equipe):
    equipe = get_object_or_404(Equipe, id=id_equipe)
    joueurs = []
    for joueur in equipe.joueurs.all():
        joueurs.append({joueur: joueur.nomJoueur})
    return render(request, 'academy/readEquipe.html', locals())

def update_equipe(request, id_equipe):
    equipe = get_object_or_404(Equipe, id=id_equipe)
    form = EquipeForm(request.POST or None, instance=equipe)
    if form.is_valid():
        form.save()
        envoi = True
    return render(request, "academy/updateEquipe.html", locals())

def delete_equipe(request, id_equipe):
    equipe = get_object_or_404(Equipe, id=id_equipe)
    if equipe:
        nom = equipe.nomEquipe
        equipe.delete()
        suppression = True
    return render(request, 'academy/deleteEquipe.html', locals())




def show_joueurs(request):
    joueurs = Joueur.objects.all()
    equipes = []
    for joueur in joueurs:
        for equipe in joueur.equipes.all():
            equipes.append({joueur.nomJoueur: equipe})
    return render(request, 'academy/joueurs.html', locals())

def read_joueur(request, id_joueur):
    joueur = get_object_or_404(Joueur, id=id_joueur)
    equipes = []
    equipesJoueur = joueur.equipes.all()
    for equipe in equipesJoueur:
        equipes.append({equipe: equipe.sport})
    return render(request, 'academy/readJoueur.html', locals())

def create_joueur(request):
    form = JoueurForm(request.POST or None)
    if form.is_valid(): 
        nomJoueur = form.cleaned_data['nomJoueur']
        form.save()
        return redirect('joueurs')
    return render(request, 'academy/createJoueur.html', locals())

def update_joueur(request, id_joueur):
    joueur = get_object_or_404(Joueur, id=id_joueur)
    form = JoueurForm(request.POST or None, instance=joueur)
    if form.is_valid():
        form.save()
        envoi = True
    return render(request, "academy/updateJoueur.html", locals())

def delete_joueur(request, id_joueur):
    joueur = get_object_or_404(Joueur, id=id_joueur)
    if joueur:
        nom = joueur.nomJoueur
        joueur.delete()
        suppression = True
    return render(request, 'academy/deleteJoueur.html', locals())

