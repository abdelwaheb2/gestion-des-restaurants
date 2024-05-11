from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    img=models.ImageField(upload_to='users',default='users/user.jpg')
    pays=models.CharField(max_length=50)
    gouvernement=models.CharField(max_length=50)
    region=models.CharField(max_length=50)
    date_n=models.DateField()
    sexe=models.CharField(max_length=1)
    def __str__(self):
        return self.user.username
    

    