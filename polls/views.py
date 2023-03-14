from django.shortcuts import render

#from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from boutique.models import Product


# Create your views here.
# We're continuing from the steps above. Append this to your caseAccras/views.py file.


def index(request):
    products = Product.objects.all()
    
    return render(request, 'main/index.html', context={"products": products})

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.sucess(request, "Votre compte à bien été créer.")
            return redirect('connexion')
        else:
            messages.error(request, form.errors)
    return render(request, 'products/register.html',{'form':form})

#def connexion(request):
    #if request.method == "POST":
        #username = request.POST['username']
        #password =request.POST['password']
        #user = authenticate(request, username=username, password=password)
        #if user is not None and user.is_active:
            #login(request, user)
            #messages.success(request, 'Bienvenue')
            #return redirect('accueil')

        #else:
            #messages.error(request, "error d'authentification")

    #return render(request, 'products/connexion.html')

#def deconnexion(request):
    #logout(request)
    #return redirect('connexion')

#@login_required #Méthode qui oblige la connexion pour cette action

def infos(request):
    return render(request, 'infos.html')

def cgv(request):
    return render(request, 'cgv.html')

def cgu(request):
    return render(request, 'cgu.html')


def mentionLegale(request):
    return render(request, 'mentionLegale.html')
