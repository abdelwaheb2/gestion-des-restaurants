from django.urls import path
from . import views


urlpatterns = [
    path('',views.accueil,name='accueil'),
    path('pub/',views.pub,name='pub'),
    path('resto<int:id>',views.plus,name='affi_resto'),
    path('inscription/',views.inscription,name='inscription'),
    path('inscription/config_resto<int:id>',views.confirmer,name='config_resto'),
    path('connexion/',views.connexion,name='connexion'),
]