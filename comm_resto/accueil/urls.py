from django.urls import path
from . import views


urlpatterns = [
    path('',views.accueil,name='accueil'),
    path('resto<int:id>',views.plus,name='affi_resto'),
    path('inscription/',views.inscription,name='inscription'),
    path('connexion/',views.connexion,name='connexion'),
    path('logout/',views.logout,name='deconnecter'),
]