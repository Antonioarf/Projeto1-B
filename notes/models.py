from django.db import models
from django.contrib.auth.models import Permission, User

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default='')
    content = models.TextField(default='')
    tag = models.CharField(max_length=50, default='')
    prazo = models.CharField(max_length=15, default='Sem Prazo')
    feito = models.BooleanField(default=False)
    users = models.ManyToManyField(User,related_name = 'dono')
    
    def __str__(self):
        return str(str(self.id) + ". " +self.title + " " + self.prazo)

