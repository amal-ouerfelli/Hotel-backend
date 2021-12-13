from django.db import models

# Create your models here.

class Chambres(models.Model):
    id_ch = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    slug = models.CharField(max_length=25)
    type = models.CharField(db_column='Type', max_length=25)  # Field name made lowercase.
    price = models.IntegerField()
    size = models.IntegerField()
    capacite = models.IntegerField()
    pets = models.CharField(max_length=25)
    breakfast = models.CharField(max_length=25)
    featured = models.CharField(max_length=25)
    description = models.TextField()
    extras = models.TextField()

    class Meta:
        managed = False
        db_table = 'chambres'

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom_et_prenm = models.CharField(db_column='nom et prenm', max_length=255)  # Field renamed to remove unsuitable characters.    
    e_mail = models.TextField()
    du = models.DateField()
    jusqua = models.DateField()

    class Meta:
        managed = False
        db_table = 'client'