from django.urls import path

from . import views

urlpatterns = [
    path('', views.PaymentsPageView.as_view(), name='payments'),
    #path('wishlist/', views.wishlist, name='wishlist'),

]