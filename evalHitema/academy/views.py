from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

def root(request):
    """ redirige http://127.0.0.1:8000 vers http://127.0.0.1:8000/academy/ """
    return redirect(accueil)

def accueil(request):
    """ page d'accueil: http://127.0.0.1:8000/academy/ """
    return render(request, 'academy/home.html')