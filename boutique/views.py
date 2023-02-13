from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.
def boucherie(request):
    return render(request, 'boucherie/Boucherie.html')

def boulangerie(request):
    return render(request, 'boulangerie/Boulangerie.html')

def epicerie(request):
    return render(request, 'epicerie/Epicerie.html')

def maraicher(request):
    return render(request, 'maraicher/Maraicher.html')

def poissonnerie(request):
    return render(request, 'poissonnerie/Poissonnerie.html')

def boissons(request):
    return render(request, 'boissons/Boissons.html')


