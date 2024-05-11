
from datetime import date
from django.shortcuts import render,redirect
from resto.models import Resto,Abonnement_resto,Plat,Evenement
from django.contrib import messages
from verif import *


# Create your views here.


def resto_admin(request,id):

    x={
        'resto':Resto.objects.get(id=id),
        'ab':len(Abonnement_resto.objects.filter(resto=id)),
        'nbp':len(Plat.objects.filter(resto=id)),
        'plats':Plat.objects.filter(resto=id,active=True)
    }
    return render(request,'resto/accueil.html',x)

def evenement(request,id):
    active=Evenement.objects.filter(resto=id,active=True)
    desactive=Evenement.objects.filter(resto=id,active=False)
    x={
        'resto':Resto.objects.get(id=id),
        'ab':len(Abonnement_resto.objects.filter(resto=id)),
        'nbp':len(Plat.objects.filter(resto=id)),
        'even_active':active,
        'even_desactive':desactive,
    }
    if request.method=='POST':
        desc=request.POST['desc']
        img=request.POST['img']
        dat=request.POST['date']
        if desc=='' or img=='' or dat=='':
            messages.info(request,'Erre')
        else:
            data=Evenement(resto=Resto(id),desc=desc,img='evenement/'+img,date=dat)
            data.save()
            return redirect('even',id)
    return render(request,'resto/even.html',x)

def desactive_e(request,id):
    data=Evenement.objects.get(id=id)
    data.active=not(data.active)
    data.save()
    return redirect('even',data.resto.id)

def suppreme_e(request,id):
    data=Evenement.objects.get(id=id)
    y=data.resto.id
    data.delete()
    return redirect('even',y)
 
def plat(request,id):
    plat=Plat.objects.filter(resto=id)
    x={
        'resto':Resto.objects.get(id=id),
        'ab':len(Abonnement_resto.objects.filter(resto=id)),
        'nbp':len(plat)
    }
    if request.method=='POST':
        nom=request.POST['nom']
        desc=request.POST['desc']
        img=request.POST['image']
        prix=request.POST['prix']
        prix=float(prix)
        if nom==''or desc=='' or img==''or prix==0:
            messages.info(request,'merci remplire tous le formulaire pour ajouter un plat')
            return redirect ('plat',x)
        else:
            data=Plat(resto=Resto(id),nom=nom,desc=desc,img='plat/'+img,prix=prix)
            data.save()
            return redirect ('accueil_resto',id) 
    return render(request,'resto/aj_plat.html',x)

def plat_d(request,id):
    x={
        'resto':Resto.objects.get(id=id),
        'ab':len(Abonnement_resto.objects.filter(resto=id)),
        'nbp':len(Plat.objects.filter(resto=id)),
        'plats':Plat.objects.filter(resto=id,active=False)
    }
    return render(request,'resto/plat_d.html',x)

def desactive_p(request,idp):
    x=Plat.objects.get(id=idp)
    x.active=not(x.active)
    x.save()
    return redirect('accueil_resto',x.resto.id)

def supp_plat(request,idp):
    x=Plat.objects.get(id=idp)
    y=x.resto.id
    x.delete()
    return redirect('accueil_resto',y)

def mod_plat(request,id):
    p=Plat.objects.get(id=id)
    x={'plat':p,
        'resto':p.resto,
        'ab':len(Abonnement_resto.objects.filter(resto=p.resto.id)),
        'nbp':len(Plat.objects.filter(resto=p.resto.id)),
    }
    if request.method=='POST':
        nom=request.POST['nom']
        desc=request.POST['desc']
        img=request.POST['image']
        prix=request.POST['prix']
        prix=float(prix)
        if img :
            p.img="plat/"+img
            p.save()
        if mot(nom)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier le nom du plat')
            x=1
        else:
            p.nom=nom
            p.save()
        if len(desc)<3:
            messages.add_message(request, messages.INFO, 'merci de verifier la description du plat')
            x=1
        else:
            p.desc=desc
            p.save()
        if prix<=0:
            messages.add_message(request, messages.INFO, 'merci de verifier le prix du plat')
            x=1
        else:
            p.prix=prix
            p.save()
        if x==1:
                return redirect('mod_plat',id)
        else:
            return redirect('accueil_resto',p.resto.id)
    return render(request,'resto/modefier_p.html',x)

def modefier_r(request,id):
    plat=Plat.objects.filter(resto=id)
    data=Resto.objects.get(id=id)
    x={'resto':data,'ab':len(Abonnement_resto.objects.filter(resto=id)),'nbp':len(plat)}
    if request.method =='POST' :
        nom=request.POST['nom']
        pre=request.POST['prenom']
        paye=request.POST['paye']
        go=request.POST['gouvernement']
        reg=request.POST['region']
        add=request.POST['addresse']
        sp=request.POST['specialite']
        desc=request.POST['description']
        img=request.POST['image']
        x=0
        if mot(nom)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre nom')
            x=1
        else:
            data.nom=nom
            data.save()
        if mot(pre)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre prenom')
            x=1
        else:
            data.pre=pre
            data.save()
        if mot(paye)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre paye')
            x=1
        else:
            data.pays=paye
            data.save()
        if mot(go)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre gouvernement')
            x=1
        else:
            data.gouvernement=go
            data.save()
        if mot(reg)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre region')
            x=1
        else:
            data.region=reg
            data.save()
        if mot_passe(add)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre addresse')
            x=1
        else:
            data.addresse=add
            data.save()
        if mot(sp)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier votre specialite')
            x=1
        else:
            data.specialite=sp
            data.save()
        if len(desc)<5:
            messages.add_message(request, messages.INFO, 'merci de verifier votre description')
            x=1
        else:
            data.desc=desc
            data.save()
        if x==1:
            return redirect('mod_resto',id)
        else:
            if img!='':
                data.image='resto/'+img
            return redirect('accueil_resto',id)

    return render(request,'resto/modefier.html',x)

