from django.forms import ModelForm
from .models import adminSysteme, agentsSancfis

class adminSystemeForm(ModelForm):
    class Meta:
        model = adminSysteme
        fields = '__all__' 

class agentsSancfisForm(ModelForm):
    class Meta:
        model = agentsSancfis
        fields = ['nom', 'prenom', 'email', 'adresse', 'ville', 'pays', 'telephone', 'motdepasse', 'profession']
        labels = {
            'motdepasse':'Mot de passe',
            'telephone': 'Téléphone',
        }
