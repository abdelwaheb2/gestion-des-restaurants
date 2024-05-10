
from django.db import models
from users.models import User



# Create your models here.
class Resto(models.Model):
    nom=models.CharField(max_length=50)
    pre=models.CharField(max_length=50)
    date_n=models.DateField()
    sexe=models.CharField(max_length=1)
    mail=models.CharField(max_length=50)
    tel=models.CharField(max_length=20)
    m_p=models.CharField(max_length=50)
    active=models.BooleanField(default=True)
    pays=models.CharField(max_length=50)
    gouvernement=models.CharField(max_length=50)
    region=models.CharField(max_length=50)
    addresse=models.CharField(max_length=50)
    img=models.ImageField(upload_to='resto') 
    specialite=models.CharField(max_length=50)
    desc=models.TextField()
    etoiles=models.IntegerField(default=0)

class Plat(models.Model):
    resto=models.ForeignKey(Resto,on_delete=models.CASCADE)
    nom=models.CharField(max_length=50)
    desc=models.TextField()
    prix=models.DecimalField(max_digits=5,decimal_places=2)
    active=models.BooleanField(default=True)
    img=models.ImageField(upload_to='plat')
    
class Commantair_plat(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pl=models.ForeignKey(Plat,on_delete=models.CASCADE)
    com=models.TextField()


class Abonnement_resto(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    resto=models.ForeignKey(Resto,on_delete=models.CASCADE)

class Evenement(models.Model):
    resto=models.ForeignKey(Resto, on_delete=models.CASCADE)
    desc=models.TextField()
    img=models.ImageField(upload_to='evenement')
    date=models.DateField()
    active=models.BooleanField(default=True)