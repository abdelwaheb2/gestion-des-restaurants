
from django.db import models

# Create your models here.
class Publicite(models.Model):
    nom=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pub')
    des=models.TextField()
    date=models.DateField()
    dure=models.IntegerField()
    active=models.BooleanField(default=True)
    

    
