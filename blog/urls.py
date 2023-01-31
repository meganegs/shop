from django.urls import path

from . import views

urlpatterns = [
    #App Blog : view 
    path('blog/', views.blog, name='bog'),
 
]