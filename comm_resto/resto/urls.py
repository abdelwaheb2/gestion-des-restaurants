
from django.urls import path
from . import views

urlpatterns = [
    path('resto<int:id>',views.resto_admin,name='accueil_resto'),
    path('plat<int:id>',views.plat,name='plat'),
    path('modefier<int:id>',views.modefier_r,name='mod_resto'),
    path('plat_d<int:id>',views.plat_d,name='plat_d'),
    path('dp<int:idp>',views.desactive_p,name='desactive'),
    path('sp<int:idp>',views.supp_plat,name='sup_plat'),
    path('mod_plat<int:id>',views.mod_plat,name='mod_plat'),
    path('evenement<int:id>',views.evenement,name='even'),
    path('de<int:id>',views.desactive_e,name='desactive_e'),
    path('se<int:id>',views.suppreme_e,name='sup_even'),


]
