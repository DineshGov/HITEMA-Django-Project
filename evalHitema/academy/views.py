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

def read_sports(request):
    sports = Sport.objects.all()
    return render(request, 'academy/sports.html', {'sports':sports})

def create_sport(request):
    form = SportForm(request.POST or None)
    if form.is_valid(): 
        nomSport = form.cleaned_data['nomSport']
        envoi = True
        form.save()
        return redirect('sports')
    return render(request, 'academy/createSport.html', locals())