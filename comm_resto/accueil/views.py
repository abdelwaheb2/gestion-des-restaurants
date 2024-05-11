
from datetime import date
from django.shortcuts import render,redirect
from resto.models import Plat, Resto,Abonnement_resto
from users.models import Users
from .models import Publicite
from django.contrib import messages
from verif import *
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User



# Create your views here.
def accueil(request):
    pub_p=Publicite.objects.get(nom='pub%principale%111')
    pub=Publicite.objects.exclude(nom='pub%principale%111')
    if request.method =='GET' :
        rech=request.GET.get('rechercher')
        if rech==None:
            x={'restos':Resto.objects.all().order_by('-etoiles'),'pub':pub,'len':range(1,len(pub)+1),'pub_p':pub_p}
        else:
            x={'restos':Resto.objects.filter(Q(nom__contains=rech) | Q(specialite__contains=rech)).order_by('nom'),
            'pub':pub,'len':range(1,len(pub)+1),
            'pub_p':pub_p,
            }
        return render(request,'accueil/accueil.html',x)
    
def deconnecter(request):
    logout(request)
    return redirect('connexion')
    
def plus(request,id):
    x={'resto':Resto.objects.get(id=id),'plats':Plat.objects.filter(resto=id,active=True)}
    return render(request,'accueil/affich_resto.html',x)

def inscription(request):
    if request.method =='POST' :
        nom=request.POST['nom']
        pre=request.POST['prenom']
        tel=request.POST['tele']
        mail=request.POST['mail']
        date=request.POST['date']
        sexe=request.POST['sexe']
        mot1=request.POST['mot']
        mot2=request.POST['conf_mot']
        x=0
        if mot(nom)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre nom')
            x=1
        if mot(pre)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre prenom')
            x=1
        elif User.objects.filter(username=tel).exists()==True  :
            messages.add_message(request, messages.INFO, 'cette username est deja utilise pour un auter compte, merci de change')
            x=1
        if dat(date)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre date naissance (l age minimale est 10 annes)')
            x=1
        if mot_passe(mot1)==False:
            messages.add_message(request, messages.INFO, 'votre mot de passe est tree faible')
            x=1
        if mot1 != mot2:
            messages.add_message(request, messages.INFO, 'merci de repeter la premier mot de passe')
        if x==1:
            return redirect('inscription')
        else:
            user = User.objects.create_user(
                username=tel,
                email=mail,
                password=mot1,
                first_name=pre,
                last_name=nom
            )
            data=Users(user=user,date_n=date,sexe=sexe)
            data.save()
            return redirect('connexion')
    return render(request,'accueil/inscription.html')




def connexion(request):
    if request.method=='POST':
        tele=request.POST['tele']
        mot=request.POST['mot_passe']
        user = authenticate(request, username=tele, password=mot)
        if user is not None:
            login(request,user)
            return redirect('acuueil_user')
        else:
            messages.info(request,'Username ou mot de passe est incorrecte')
            return redirect('connexion')
           
        
    
    return render(request,'accueil/connexion.html')

