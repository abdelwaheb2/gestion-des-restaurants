from django.db.models import Count
from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Users
from resto.models import Abonnement_resto, Evenement,Resto,Plat
from verif import *
from django.contrib import messages
# Create your views here.
def create_restau(request):
    user=Users.objects.get(user=request.user)
    if request.method=='POST':
        nom=request.POST['nom']
        paye=request.POST['paye']
        go=request.POST['gouvernement']
        reg=request.POST['region']
        add=request.POST['addresse']
        img=request.POST['image']
        sp=request.POST['specialite']
        desc=request.POST['description']
        x=0
        if mot(nom)==False:
            messages.add_message(request, messages.INFO, 'merci de verifier nom de votre restaurant ')
            x=1
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
            return redirect('create_restau',id)
        else:
            data=Resto()
            data.chef=Users.objects.get(user=request.user)
            data.nom=nom
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

def resto_admin(request):

    x={
        'resto':Resto.objects.get(id=id),
        'ab':len(Abonnement_resto.objects.filter(resto=id)),
        'nbp':len(Plat.objects.filter(resto=id)),
        'plats':Plat.objects.filter(resto=id,active=True)
    }
    return render(request,'resto/accueil.html',x)

def accueil(request):
    user=Users.objects.get(user=request.user)
    plats=[]
    ab=Abonnement_resto.objects.filter(user=user)

    if request.method=='GET':
        rech=request.GET.get('rech')
        if rech==None or rech=='':
            rech=''
            for i in ab:
                plats.append(Plat.objects.filter(resto=i.resto))
        else:
            for i in ab:
                plats.append(Plat.objects.filter(Q(nom__contains=rech) | Q(desc__contains=rech),resto=i.resto))
                

    x={'user':user,'plats':plats,'rech':rech}
    return render(request,'user/accueil.html',x)

def even(request):
    user=Users.objects.get(user=request.user)
    ab=Abonnement_resto.objects.filter(user=user.id)
    even=[]
    for i in ab:
        even.append(Evenement.objects.filter(resto=i.resto))

    x={'user':user,'even':even}
    return render(request,'user/even.html',x)

def resto_plats(request,idr):
    user=Users.objects.get(user=request.user)
    if Abonnement_resto.objects.filter(resto=idr,user=user.id).exists()==False:
        x='Abonne'
    else:
        x='Desabonne'
    x={'plats':Plat.objects.filter(resto=idr,active=True),
        'resto':Resto.objects.get(id=idr),
        'user':user,
        'ab':x,
        'nb_ab':len(Abonnement_resto.objects.filter(resto=idr))
    }
    return render(request,'user/resto_p.html',x)

def resto_evenement(request,idr):
    user=Users.objects.get(user=request.user)
    if Abonnement_resto.objects.filter(resto=idr,user=user.id).exists()==False:
        x='Abonne'
    else:
        x='Desabonne'
    x={'resto':Resto.objects.get(id=idr),
    'user':Users.objects.get(user=request.user),
    'even':Evenement.objects.filter(resto=idr,active=True),
    'ab':x,
    'nb_ab':len(Abonnement_resto.objects.filter(resto=idr))
    }
    return render(request,'user/resto_e.html',x)

def abonnement(request,idr):
    user=Users.objects.get(user=request.user)
    if Abonnement_resto.objects.filter(resto=idr,user=user.id).exists()==False:
        data=Abonnement_resto(resto=Resto(idr),user=user)
        data.save()
        return redirect('plats_resto',idr)
    else:
        data=Abonnement_resto.objects.filter(resto=idr,user=user.id)
        data.delete()
        return redirect('plats_resto',idr)
    

def restos(request):
    voir_plus=[]
    user=Users.objects.get(user=request.user)
    if request.method=='GET':
        rech=request.GET.get('rech')
        if rech==None or rech=='':
            resto=Resto.objects.all()
        else:
            resto=Resto.objects.filter(nom=rech).order_by('nom')
            plus=Resto.objects.filter(Q(nom__contains=rech) | Q(specialite__contains=rech)).order_by('nom')
            for i in plus:
                if Abonnement_resto.objects.filter(user=user.id,resto=i.id).exists()==False:
                    voir_plus.append(i)
    restos=[]
    for i in resto:
        if Abonnement_resto.objects.filter(user=user.id,resto=i.id).exists()==False:
            restos.append(i)

   
    x={'user':user,'restos':restos,'plus':voir_plus}
    return render(request,'user/restos.html',x)

def modefier(request):
    data=Users.objects.get(user=request.user)
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
            return redirect('mod_Users',id)
        else:
            data.img='users/'+img
            data.save()
            return redirect('acuueil_user')


    return render(request,'user/modefier.html',x)

def resto_ab(request):
    user=Users.objects.get(user=request.user)
    ab=Abonnement_resto.objects.filter(user=user)
    restos=[]
    for i in ab:
        restos.append(Resto.objects.get(id=i.resto.id))

    x={'restos':restos,'user':user}
    return render(request,'user/resto_ab.html',x)


def myrestaus(request):
    user=Users.objects.get(user=request.user)
    restaus = Resto.objects.filter(chef=user).annotate(nbr=Count('abonnement_resto'))
    return render(request,'user/myrestaus.html',{"restaus" : restaus,"user":user})

