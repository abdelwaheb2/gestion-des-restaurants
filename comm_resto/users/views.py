
from django.shortcuts import render,redirect
from django.db.models import Q
from .models import User
from resto.models import Abonnement_resto, Evenement,Resto,Plat
from verif import *
from django.contrib import messages
# Create your views here.


def accueil(request,id):
    plats=[]
    voir_plus=[]
    ab=Abonnement_resto.objects.filter(user=id)

    if request.method=='GET':
        rech=request.GET.get('rech')
        if rech==None or rech=='':
            rech=''
            for i in ab:
                plats.append(Plat.objects.filter(resto=i.resto))
        else:
            for i in ab:
                plats.append(Plat.objects.filter(nom=rech,resto=i.resto))
                voir_plus.append(Plat.objects.filter(nom__contains=rech,resto=i.resto))

    x={'user':User.objects.get(id=id),'plats':plats,'plus':voir_plus,'rech':rech}
    return render(request,'user/accueil.html',x)

def even(request,id):
    ab=Abonnement_resto.objects.filter(user=id)
    even=[]
    for i in ab:
        even.append(Evenement.objects.filter(resto=i.resto))

    x={'user':User.objects.get(id=id),'even':even}
    return render(request,'user/even.html',x)

def resto_plats(request,idr,idu):
    if Abonnement_resto.objects.filter(resto=idr,user=idu).exists()==False:
        x='Abonne'
    else:
        x='Desabonne'
    x={'plats':Plat.objects.filter(resto=idr,active=True),
    'resto':Resto.objects.get(id=idr),
    'user':User.objects.get(id=idu),
    'ab':x,
    'nb_ab':len(Abonnement_resto.objects.filter(resto=idr))
    }
    return render(request,'user/resto_p.html',x)

def resto_evenement(request,idr,idu):
    if Abonnement_resto.objects.filter(resto=idr,user=idu).exists()==False:
        x='Abonne'
    else:
        x='Desabonne'
    x={'resto':Resto.objects.get(id=idr),
    'user':User.objects.get(id=idu),
    'even':Evenement.objects.filter(resto=idr,active=True),
    'ab':x,
    'nb_ab':len(Abonnement_resto.objects.filter(resto=idr))
    }
    return render(request,'user/resto_e.html',x)

def abonnement(request,idr,idu):
    if Abonnement_resto.objects.filter(resto=idr,user=idu).exists()==False:
        data=Abonnement_resto(resto=Resto(idr),user=User(idu))
        data.save()
        return redirect('plats_resto',idr,idu)
    else:
        data=Abonnement_resto.objects.filter(resto=idr,user=idu)
        data.delete()
        return redirect('acuueil_user',idu)
    

def restos(request,id):
    voir_plus=[]
    if request.method=='GET':
        rech=request.GET.get('rech')
        if rech==None or rech=='':
            resto=Resto.objects.all()
        else:
            resto=Resto.objects.filter(Q(nom=rech) | Q(pre=rech)).order_by('nom')
            plus=Resto.objects.filter(Q(nom__contains=rech) | Q(pre__contains=rech)).order_by('nom')
            for i in plus:
                if Abonnement_resto.objects.filter(user=id,resto=i.id).exists()==False:
                    voir_plus.append(i)
    restos=[]
    for i in resto:
        if Abonnement_resto.objects.filter(user=id,resto=i.id).exists()==False:
            restos.append(i)

   
    x={'user':User.objects.get(id=id),'restos':restos,'plus':voir_plus}
    return render(request,'user/restos.html',x)

def modefier(request,id):
    data=User.objects.get(id=id)
    x={'user':data}
    if request.method =='POST' :
        nom=request.POST['nom']
        pre=request.POST['prenom']
        paye=request.POST['paye']
        go=request.POST['gouvernement']
        reg=request.POST['region']
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
        if x==1:
            return redirect('mod_user',id)
        else:
            data.img='users/'+img
            data.save()
            return redirect('acuueil_user',id)


    return render(request,'user/modefier.html',x)

def resto_ab(request,id):
    ab=Abonnement_resto.objects.filter(user=id)
    restos=[]
    for i in ab:
        restos.append(Resto.objects.get(id=i.resto.id))

    x={'restos':restos,'user':User.objects.get(id=id)}
    return render(request,'user/resto_ab.html',x)


