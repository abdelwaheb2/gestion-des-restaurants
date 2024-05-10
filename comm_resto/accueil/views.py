
from datetime import date
from django.shortcuts import render,redirect
from resto.models import Plat, Resto,Abonnement_resto
from users.models import User
from .models import Publicite
from django.contrib import messages
from verif import *
from django.db.models import Q



# Create your views here.
def accueil(request):
    pub_p=Publicite.objects.get(nom='pub%principale%111')
    pub=Publicite.objects.exclude(nom='pub%principale%111')
    if request.method =='GET' :
        rech=request.GET.get('rechercher')
        if rech==None:
            x={'restos':Resto.objects.all().order_by('-etoiles'),'pub':pub,'len':range(1,len(pub)+1),'pub_p':pub_p}
        else:
            x={'restos':Resto.objects.filter(Q(nom=rech) | Q(pre=rech)).order_by('nom'),
            'pub':pub,'len':range(1,len(pub)+1),
            'pub_p':pub_p,
            'voir':Resto.objects.filter(Q(nom__contains=rech) | Q(pre__contains=rech)).order_by('nom')
            }
        return render(request,'accueil/accueil.html',x)
    
def pub (request):
    pub_p=Publicite.objects.get(nom='pub%principale%111')
    pub=Publicite.objects.exclude(nom='pub%principale%111')
    x={'pub':pub,'len':range(1,len(pub)+1),'pub_p':pub_p}
    if request.method=='POST':
        nom=request.POST['nom']
        desc=request.POST['desc']
        img=request.POST['img']
        dure=request.POST['dure']
        if nom=='' or desc=='' or img=='' or dure=='0':
            messages.info(request,'erre')
        else:
            data=Publicite(nom=nom,des=desc,img='pub/'+img,dure=dure,date=date.today())
            data.save()
            return redirect('pub')
    return render (request,'accueil/cree_pub.html',x)
    
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
        compte=request.POST['compte']
        x=0
        if mot(nom)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre nom')
            x=1
        if mot(pre)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre prenom')
            x=1
        if tele(tel)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre numero de telephone')
            x=1
        elif User.objects.filter(tel=tel).exists()==True or Resto.objects.filter(tel=tel).exists()==True :
            messages.add_message(request, messages.INFO, 'cette numero de telephone est deja utilise pour un auter compte, merci de change')
            x=1
        if dat(date)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre date naissance (l age minimale est 10 annes)')
            x=1
        if mot_passe(mot1)==False:
            messages.add_message(request, messages.INFO, 'votre mot de passe est tree faible')
            x=1
        if mot1 != mot2:
            messages.add_message(request, messages.INFO, 'merci de repeter la premier mot de passe')
        if compte=='0':
            messages.add_message(request, messages.INFO, 'merci de choix la nature de votre compte')
            x=1
        if x==1:
            return redirect('inscription')
        else:
            if compte=='2':
                data=Resto(nom=nom,pre=pre,date_n=date,sexe=sexe,mail=mail,tel=tel,m_p=mot1)
                data.save()
                return redirect('config_resto',data.id)
            else:
                data=User(nom=nom,pre=pre,date_n=date,sexe=sexe,mail=mail,tel=tel,m_p=mot1)
                data.save()
                return redirect('acuueil_user',data.id)
    return render(request,'accueil/inscription.html')


def confirmer(request,id):
    data=Resto.objects.get(id=id)
    if request.method=='POST':
        mail=request.POST['mail']
        paye=request.POST['paye']
        go=request.POST['gouvernement']
        reg=request.POST['region']
        add=request.POST['addresse']
        img=request.POST['image']
        sp=request.POST['specialite']
        desc=request.POST['description']
        x=0
        if mot(paye)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre paye')
            x=1
        if mot(go)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre gouvernement')
            x=1
        if mot(reg)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre region')
            x=1
        if mot_passe(add)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre addresse')
            x=1
        if img=='':
            messages.add_message(request, messages.INFO, 'importe la logo de votre resto')
            x=1
        if mot(sp)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre specialite')
            x=1
        if x==1:
            return redirect('config_resto',id)
        else:
            data.pays=paye
            data.gouvernement=go
            data.region=reg
            data.addresse=add
            data.img='resto/'+img
            data.specialite=sp
            data.desc=desc
            data.save()
            return redirect('accueil_resto',data.id)
    return render(request,'accueil/config_resto.html')

def connexion(request):
    if request.method=='POST':
        tele=request.POST['tele']
        mot=request.POST['mot_passe']
        if User.objects.filter(tel=tele).exists()==True:
            if User.objects.filter(m_p=mot).exists()==False:
                messages.info(request,'mot de passe incorrect')
                return redirect('connexion')
            else:
                x=User.objects.get(tel=tele)
                return redirect('acuueil_user',x.id)
        elif Resto.objects.filter(tel=tele).exists()==True:
           if Resto.objects.filter(m_p=mot).exists()==False:
                messages.info(request,'mot de passe incorrect')
                return redirect('connexion')
           else:
                x=Resto.objects.get(tel=tele)
                return redirect('accueil_resto',x.id)
        else:
            messages.info(request,'acune compte avec cette numero de telephone')
    
    return render(request,'accueil/connexion.html')

