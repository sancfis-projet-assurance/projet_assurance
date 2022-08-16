from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AdminSysteme(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=20, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    profession = models.CharField(max_length=40, null=True)
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)
    

class AgentSancfis(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    adresse = models.CharField(max_length=40, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=20, null=True)
    profession = models.CharField(max_length=40, null=True)
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.telephone

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)

class AgentAssurance(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    adresse = models.CharField(max_length=40, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    profession = models.CharField(max_length=40, null=True)
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.telephone

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)


class AgentLaboratoire(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    adresse = models.CharField(max_length=40, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    profession = models.CharField(max_length=40, null=True)
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.telephone
     
    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)
    
class AgentPharmacie(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    adresse = models.CharField(max_length=40, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    profession = models.CharField(max_length=40, null=True)
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.telephone

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)
    

class AgentCs(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    adresse = models.CharField(max_length=40, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    profession = models.CharField(max_length=40, null=True)
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.telephone

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)
    
    
class Employe(models.Model):

    dateEmbauche = models.DateField()
    dateResiliation = models.DateField()
    statut = models.BooleanField()
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.dateEmbauche

class Assurance(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    designation = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    longitude = models.FloatField(max_length=20, null=True)
    latitude = models.FloatField(max_length=20, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)


class Laboratoire(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    designation = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    longitude = models.FloatField(max_length=40, null=True)
    latitude = models.FloatField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)


class Pharmacie(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    designation = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    longitude = models.FloatField(max_length=40, null=True)
    latitude = models.FloatField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)

    
class centreDeSoins(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    designation = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    longitude = models.FloatField(max_length=40, null=True)
    latitude = models.FloatField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)

    
class Souscripteur(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    designation = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    longitude = models.FloatField(max_length=40, null=True)
    latitude = models.FloatField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs) 

    
class Assure(models.Model):

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    numero = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    dateNaiss = models.DateField()
    lieuNaiss = models.CharField(max_length=40, null=True)
    taille = models.FloatField(max_length=4, null=True)
    masse = models.FloatField(max_length=6, null=True)
    ville = models.CharField(max_length=40, null=True)
    pays = models.CharField(max_length=40, null=True)
    defautSante = models.CharField(max_length=40, null=True)
    profession = models.CharField(max_length=40, null=True)  
    ayantDroit = models.BooleanField()    
    statut = models.BooleanField()
    CHOIX = (
        ('MASCULIN', 'masculin'),
        ('FEMININ', 'feminin'),
    )
    genre = models.CharField(max_length=10, choices=CHOIX, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)

class policeAssurance(models.Model):

    numero = models.CharField(max_length=40)
    taux = models.IntegerField()
    datePriseEffet = models.DateField()
    dateFin = models.DateField()
    statutModification = models.BooleanField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.numero

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

class Pays(models.Model):
    pays=models.CharField(max_length=40)

class Ville(models.Model):
    pays=models.ForeignKey(Pays, on_delete=models.CASCADE)
    ville=models.CharField(max_length=40)
    
class Taille(models.Model):
    taille=models.CharField(max_length=5)

class Quantite(models.Model):
    qtite=models.CharField(max_length=20)

class Forme(models.Model):
    forme=models.CharField(max_length=30)

class Moment(models.Model):
    moment=models.CharField(max_length=20)

class Periode(models.Model):
    periode=models.CharField(max_length=20)

class Profession(models.Model):
    profession=models.CharField(max_length=40)

class Masse(models.Model):
    masse=models.CharField(max_length=8)

class Prix(models.Model):
    prix=models.FloatField(max_length=40)
    objects = models.Manager()

class Dosage(models.Model):
    dosage=models.CharField(max_length=20)

class Frequence(models.Model):
    frequence=models.CharField(max_length=20)

class Specialite(models.Model):
    specialite=models.CharField(max_length=40)

class voieAdministration(models.Model):
    voie=models.CharField(max_length=40)

