from django.contrib import admin
from django.urls import path, include
from contact.views import contact
from polls.views import accueil, connexion, deconnexion, register, cgu, cgv,infos, mentionLegale
from boutique.views import boucherie, boulangerie, epicerie, maraicher, boissons, poissonnerie
from blog.views import blog



urlpatterns = [
    path('', accueil, name='accueil'),
    path('admin/', admin.site.urls),
    path('payments/', include('payments.urls')),
    path('contact/', contact, name='contact'),

    #App Polls : Authentification path
    path('register/', register, name='register'),
    path('login/', connexion, name='login'),
    path('logout/', deconnexion, name='logout'),

    #App Boutique : view 
    path('boissons/', boissons, name='boissons'),
    path('poissonnerie/', poissonnerie, name='poissonnerie'),
    path('maraicher/', maraicher, name='maraicher'),
    path('epicerie/', epicerie, name='epicerie'),
    path('boucherie/', boucherie, name='boucherie'),
    path('boulangerie/', boulangerie, name='boulangerie'),

    #About
    path('infos/', infos, name='infos'),
    path('blog/', blog, name='blog'),
    path('cgu/', cgu, name='cgu'),
    path('cgv/', cgv, name='cgv'),
    path('mentionLegale/', mentionLegale, name='mentionLegale'),




]
