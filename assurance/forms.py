from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class creerUtillisateur(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username': 'Nom utilisateur',
            'first_name': 'Nom',
            'last_name': 'Prénom',
            'email': 'Email',
            'password1': 'Mot de passe',
            'password2': 'Confirmer le mot de passe'
        }

class adminSystemeForm(forms.ModelForm):
    class Meta:
        model = AdminSysteme
        fields = ['adresse', 'telephone', 'ville', 'pays', 'profession', 'genre'] 

class assureForm(forms.ModelForm):
    class Meta:
        model = Assure
        fields = ['numero', 'adresse', 'telephone', 'dateNaiss', 'lieuNaiss', 'taille', 
                        'masse', 'ville', 'pays', 'defautSante', 'profession', 'ayantDroit', 'genre', 'statut']
        labels = {
            'numero': 'Numéro',
            'dateNaiss': 'Date de Naissance',
            'lieuNaiss': 'Lieu de Naissance',
            'taille': 'Taille',
            'masse': 'Masse',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'pays': 'Pays',
            'defautSante': 'Defaut de Santé',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'ayantDroit': '',
            'genre': 'Genre',
            'statut': 'Etat'
        }

class assuranceForm(forms.ModelForm):
    class Meta:
        model = Assurance
        fields = ['designation', 'adresse', 'telephone', 'ville', 'pays', 'longitude', 'latitude' ]
        labels = {
            'designation': 'Designation',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'pays': 'Pays',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'longitude': 'Longitude',
            'Latitude': 'Latitude'
        }

class pharmacieForm(forms.ModelForm):
    class Meta:
        model = Pharmacie
        fields = ['designation', 'adresse', 'telephone', 'ville', 'pays', 'longitude', 'latitude' ]
        labels = {
            'designation': 'Designation',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'pays': 'Pays',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'longitude': 'Longitude',
            'Latitude': 'Latitude'
        }

class laboratoireForm(forms.ModelForm):
    class Meta:
        model = Laboratoire
        fields = ['designation', 'adresse', 'telephone', 'ville', 'pays', 'longitude', 'latitude' ]
        labels = {
            'designation': 'Designation',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'pays': 'Pays',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'longitude': 'Longitude',
            'Latitude': 'Latitude'
        }

class csForm(forms.ModelForm):
    class Meta:
        model = centreDeSoins
        fields = ['designation', 'adresse', 'telephone', 'ville', 'pays', 'longitude', 'latitude' ]
        labels = {
            'designation': 'Designation',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'pays': 'Pays',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'longitude': 'Longitude',
            'Latitude': 'Latitude'
        }
class agentSancfisForm(forms.ModelForm):
    class Meta:
        model = AgentSancfis
        fields = ['adresse', 'ville', 'pays', 'telephone', 'profession', 'genre']
        labels = {
            'adresse': 'Adresse',
            'ville': 'Ville',
            'pays': 'Pays',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'genre': 'Genre'
        }

class agentAssuranceForm(forms.ModelForm):
    class Meta:
        model = AgentAssurance
        fields = ['adresse', 'ville', 'pays', 'telephone', 'profession', 'genre']
        labels = {
            'adresse': 'Adresse',
            'ville': 'Ville',
            'pays': 'Pays',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'genre': 'Genre'
        }

class agentCsForm(forms.ModelForm):
    class Meta:
        model = AgentCs
        fields = ['adresse', 'ville', 'pays', 'telephone', 'profession', 'genre']
        labels = {
            'adresse': 'Adresse',
            'ville': 'Ville',
            'pays': 'Pays',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'genre': 'Genre'
        }

class agentLaboratoireForm(forms.ModelForm):
    class Meta:
        model = AgentLaboratoire
        fields = ['adresse', 'ville', 'pays', 'telephone', 'profession', 'genre']
        labels = {
            'adresse': 'Adresse',
            'ville': 'Ville',
            'pays': 'Pays',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'genre': 'Genre'
        }

class agentPharmacieForm(forms.ModelForm):
    class Meta:
        model = AgentPharmacie
        fields = ['adresse', 'ville', 'pays', 'telephone', 'profession', 'genre']
        labels = {
            'adresse': 'Adresse',
            'ville': 'Ville',
            'pays': 'Pays',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'genre': 'Genre'
        }

class souscripteurForm(forms.ModelForm):
    class Meta:
        model = Souscripteur
        fields = ['designation', 'adresse', 'telephone', 'ville', 'pays', 'longitude', 'latitude' ]
        labels = {
            'designation': 'Designation',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'pays': 'Pays',
            'telephone': 'Téléphone',
            'profession': 'Profession',
            'longitude': 'Longitude',
            'Latitude': 'Latitude'
        }

class employeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['dateEmbauche', 'dateResiliation', 'statut', 'genre']
        labels = {
            'dateEmbauche': 'Date Embauche',
            'dateResiliation': 'Date Resiliation',
            'statut': 'Statut',
            'genre': 'Genre',
        }

