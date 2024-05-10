from django.db import models

# Create your models here.
class User(models.Model):
    nom=models.CharField(max_length=50)
    pre=models.CharField(max_length=50)
    img=models.ImageField(upload_to='users',default='users/user.jpg')
    pays=models.CharField(max_length=50)
    gouvernement=models.CharField(max_length=50)
    region=models.CharField(max_length=50)
    date_n=models.DateField()
    sexe=models.CharField(max_length=1)
    mail=models.CharField(max_length=50)
    tel=models.CharField(max_length=50)
    m_p=models.CharField(max_length=50)
    

    