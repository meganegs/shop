from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    prenoms = models.CharField(max_length=200, db_index=True)
    date_de_naissance = models.CharField(max_length=200, db_index=True)
    date_inscription = models.CharField(max_length=200, db_index=True)
    postal_addresse = models.CharField(max_length=200, db_index=True)
    email = models.CharField(max_length=200, db_index=True)
    password = models.CharField(max_length=50)


class Livreur(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    prenoms = models.CharField(max_length=200, db_index=True)
    date_de_naissance = models.CharField(max_length=200, db_index=True)
    date_inscription = models.CharField(max_length=200, db_index=True)
    postal_addresse = models.CharField(max_length=200, db_index=True)
    adresse_facturation = models.CharField(max_length=200)
    email = models.CharField(max_length=200, db_index=True)
    password = models.CharField(max_length=50)

