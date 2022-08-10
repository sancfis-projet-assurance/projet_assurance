from django.db import models
from django.contrib.auth.models import AbstractUser
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
    adminSysteme = models.ForeignKey(adminSysteme, on_delete=models.CASCADE, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return self.nom

class agentAssurance(models.Model):
     nomAgent=models.CharField(max_length=40)
     prenomAgent=models.CharField(max_length=40)
     adresseAgent=models.CharField(max_length=40)
     telAgent=models.CharField(max_length=15)
     emailAgent = models.EmailField(unique=True)
     passwordAgent=models.CharField(max_length=40)
     profession=models.CharField(max_length=40)
     
     #renommer l'instance du modèle avec son nom de titre
     def __str__(self):
          return self.nomAgent

class agentLaboratoire(models.Model):
     nomAgent=models.CharField(max_length=40)
     prenomAgent=models.CharField(max_length=40)
     adresseAgent=models.CharField(max_length=40)
     telAgent=models.CharField(max_length=15)
     emailAgent = models.EmailField(unique=True)
     passwordAgent=models.CharField(max_length=40)
     profession=models.CharField(max_length=40)
     
     def __str__(self):
          return self.nomAgent

class agentPharmacie(models.Model):
     nomAgent=models.CharField(max_length=40)
     prenomAgent=models.CharField(max_length=40)
     adresseAgent=models.CharField(max_length=40)
     telAgent=models.CharField(max_length=15)
     emailAgent = models.EmailField(unique=True)
     passwordAgent=models.CharField(max_length=40)
     profession=models.CharField(max_length=40)
     
     def __str__(self):
          return self.nomAgent

class agentCs(models.Model):
     nomAgent=models.CharField(max_length=40)
     prenomAgent=models.CharField(max_length=40)
     adresseAgent=models.CharField(max_length=40)
     telAgent=models.CharField(max_length=15)
     emailAgent = models.EmailField(unique=True)
     passwordAgent=models.CharField(max_length=40)
     profession=models.CharField(max_length=40)
     
     def __str__(self):
          return self.nomAgent


class employe(models.Model):
    dateEmbauche=models.DateField()
    dateResiliation=models.DateField()
    statut=models.BooleanField()

class Assurance(models.Model):
     nomAssurance=models.CharField(max_length=40)
     adresseAssurance=models.CharField(max_length=40)
     telAssurance=models.CharField(max_length=15)
     emailAssurance = models.EmailField(unique=True)
     passwordAssurance=models.CharField(max_length=40)
     ville=models.CharField(max_length=40)
     longitude=models.CharField(max_length=40)
     latitude=models.CharField(max_length=40)

     def __str__(self):
          return self.nomAssurance


class Laboratoire(models.Model):
     nomLaboratoire=models.CharField(max_length=40)
     adresseLaboratoire=models.CharField(max_length=40)
     telLaboratoire=models.CharField(max_length=15)
     emailLaboratoire= models.EmailField(unique=True)
     passwordLaboratoire=models.CharField(max_length=40)
     ville=models.CharField(max_length=40)
     longitude=models.CharField(max_length=40)
     latitude=models.CharField(max_length=40)

     def __str__(self):
          return self.nomLaboratoire

class Pharmacie(models.Model):
     nomPharmacie=models.CharField(max_length=40)
     adressePharmacie=models.CharField(max_length=40)
     telPharmacie=models.CharField(max_length=15)
     emailPharmacie= models.EmailField(unique=True)
     passwordPharmacie=models.CharField(max_length=40)
     ville=models.CharField(max_length=40)
     longitude=models.CharField(max_length=40)
     latitude=models.CharField(max_length=40)

     def __str__(self):
          return self.nomPharmacie

class CentreDeSoins(models.Model):
     nomCentreDeSoins=models.CharField(max_length=40)
     adresseCentreDeSoins=models.CharField(max_length=40)
     telCentreDeSoins=models.CharField(max_length=15)
     emailCentreDeSoins= models.EmailField(unique=True)
     passwordCentreDeSoins=models.CharField(max_length=40)
     ville=models.CharField(max_length=40)
     longitude=models.CharField(max_length=40)
     latitude=models.CharField(max_length=40)

     def __str__(self):
          return self.nomCentreDeSoins

class Souscripteur(models.Model):
     nomSouscripteur=models.CharField(max_length=40)
     adresseSouscripteur=models.CharField(max_length=40)
     telSouscripteur=models.CharField(max_length=15)
     emailSouscripteur= models.EmailField(unique=True)
     passwordSouscripteur=models.CharField(max_length=40)
     ville=models.CharField(max_length=40)
     longitude=models.CharField(max_length=40)
     latitude=models.CharField(max_length=40) 

     def __str__(self):
          return self.nomSouscripteur

class Assure(models.Model):
     numeroAssure=models.CharField(40)
     nomAssure=models.CharField(max_length=40)
     prenomAssure=models.CharField(max_length=40)
     adresseAssure=models.CharField(max_length=40)
     telAssure=models.CharField(max_length=15)
     emailAssure= models.EmailField(unique=True)
     passwordAssure=models.CharField(max_length=40)
     dateNaissAssure=models.DateField()
     lieuNaissAssure=models.CharField(max_length=40)
     taille=models.CharField(max_length=40)
     masse=models.CharField(max_length=40)
     ville=models.CharField(max_length=40)
     defautSante=models.CharField(max_length=40)
     profession=models.CharField(max_length=40)  
     ayantDroit=models.BooleanField()    
     statut=models.BooleanField()

class PoliceAssurance(models.Model):
    numeroPoliceAssurance=models.CharField(max_length=40)
    taux=models.DecimalField(max_digits=5)
    datePriseEffet=models.DateField()
    dateFin=models.DateField()
    statutModification=models.BooleanField()

class Prestation(models.Model):
    libellePrestation=models.CharField(max_length=40)

class Examen(models.Model):
    libelleExamen=models.CharField(max_length=40)

class Consultation(models.Model):
    libelleConsultation=models.CharField(max_length=40)

class Medicament(models.Model):
    libelleMedicament=models.CharField(max_length=40)

class Ordonnance(models.Model):
    numeroOrdonnance=models.CharField(max_length=40)

class pays(models.Model):
    pays=models.CharField(max_length=40)

class ville(models.Model):
    pays=models.ForeignKey(pays, on_delete=models.CASCADE)
    ville=models.CharField(max_length=40)
    
class taille(models.Model):
    taille=models.CharField(max_length=5)

class quantite(models.Model):
    qtite=models.CharField(max_length=20)

class forme(models.Model):
    forme=models.CharField(max_length=30)

class moment(models.Model):
    moment=models.CharField(max_length=20)

class periode(models.Model):
    periode=models.CharField(max_length=20)

class profession(models.Model):
    profession=models.CharField(max_length=40)

class masse(models.Model):
    masse=models.CharField(max_length=8)

class prix(models.Model):
    prix=models.FloatField(max_length=40)

class dosage(models.Model):
    dosage=models.CharField(max_length=20)

class frequence(models.Model):
    frequence=models.CharField(max_length=20)

class specialite(models.Model):
    specialite=models.CharField(max_length=40)

class voieAdministration(models.Model):
    voie=models.CharField(max_length=40)
