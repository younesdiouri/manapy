from django.db import models

# Create your models here.
class Users(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    rank = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de creation")
    def __str__(self):
        return self.nom

class Tasks(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    checked = models.IntegerField()
    contenu = models.TextField(null=True)
    categorie = models.CharField(max_length=100)
    users = models.ManyToManyField(Users)
    date_creation = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de creation")
    date_fin = models.DateTimeField(null=True,blank=True,
                                verbose_name="Echeance")
    def __str__(self):
        return self.titre

