
from django.urls import path
from . import views

urlpatterns = [
    path('',views.accueil,name='acuueil_user'),
    path('resto/<int:idr>',views.resto_plats,name='plats_resto'),
    path('resto/evenement/<int:idr>',views.resto_evenement,name='even_resto'),
    path('modefier',views.modefier,name='mod_user'),
    path('abonnement',views.resto_ab,name='resto_ab'),
    path('restos',views.restos,name='restos'), 
    path('ab<int:idr>',views.abonnement,name='abonne'),
    path('evenement',views.even,name='even_user'),
    path('create_restau',views.create_restau,name='create_restau'),
    path('myRestaus',views.myrestaus,name='myrestaus'),
]