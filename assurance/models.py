from asyncio import Task
from django.db import models

# Create your models here.

class adminSysteme(models.Model):
    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=100, null=True)
    adresse = models.CharField(max_length=40, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=20, null=True)
    motdepasse = models.CharField(max_length=25, null=True)
    profession = models.CharField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom

class agentsSancfis(models.Model):
    nom = models.CharField(max_length=40, null=True)
    prenom = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=100, null=True)
    adresse = models.CharField(max_length=40, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=20, null=True)
    motdepasse = models.CharField(max_length=25, null=True)
    profession = models.CharField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True, null=True)
    admin_systeme = models.ForeignKey(adminSysteme, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        try:
            self.admin_systeme
        except:
            self.admin_systeme = adminSysteme.objects.first()
        super().save(*args, **kwargs)
