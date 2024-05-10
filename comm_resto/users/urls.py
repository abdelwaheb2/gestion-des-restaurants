
from django.urls import path
from . import views

urlpatterns = [
    path('usercompte<int:id>',views.accueil,name='acuueil_user'),
    path('resto/<int:idr>/<int:idu>',views.resto_plats,name='plats_resto'),
    path('resto/evenement/<int:idr>/<int:idu>',views.resto_evenement,name='even_resto'),
    path('modefier<int:id>',views.modefier,name='mod_user'),
    path('abonnement<int:id>',views.resto_ab,name='resto_ab'),
    path('restos<int:id>',views.restos,name='restos'), 
    path('ab<int:idr>/<int:idu>',views.abonnement,name='abonne'),
    path('evenement<int:id>',views.even,name='even_user'),
]