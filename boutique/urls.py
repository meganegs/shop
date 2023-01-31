from django.urls import path

from . import views

urlpatterns = [
    #App Boutique : view 
    path('boissons/', views.boissons, name='boissons'),
    path('poissonnerie/', views.poissonnerie, name='poissonnnerie'),
    path('maraicher/', views.maraicher, name='maraicher'),
    path('epicerie/', views.epicerie, name='epicerie'),
    path('boucherie/', views.boucherie, name='boucherie'),
    path('boulangerie/', views.boulangerie, name='boulangerie'),

]