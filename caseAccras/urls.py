from django.contrib import admin
from django.urls import path, include
from polls.views import index, cgu, cgv,infos, mentionLegale
from boutique.views import boucherie, boulangerie, epicerie, maraicher, boissons, poissonnerie, login, logout, callback
from payments.views import wishlist 
from contact.views import contact



urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('payments/', include('payments.urls')),
    path('contact/', contact, name='contact'),

    #App Polls : Authentification path
    #path('register/', register, name='register'),
    #path('connexion/', connexion, name='connexion'),
    #path('deconnexion/', deconnexion, name='deconnexion'),

    #App Boutique : view 
    path('boissons/', boissons, name='boissons'),
    path('poissonnerie/', poissonnerie, name='poissonnerie'),
    path('maraicher/', maraicher, name='maraicher'),
    path('epicerie/', epicerie, name='epicerie'),
    path('boucherie/', boucherie, name='boucherie'),
    path('boulangerie/', boulangerie, name='boulangerie'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('callback/', callback, name='callback'),


    #About
    path('infos/', infos, name='infos'),
    path('cgu/', cgu, name='cgu'),
    path('cgv/', cgv, name='cgv'),
    path('mentionLegale/', mentionLegale, name='mentionLegale'),

    #Cart
    path('wishlist/', wishlist, name='wishlist'),

]
