from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group
from assurance.forms import *
from assurance.models import *
from .privileges import *

# AUTHENTIFICATION

@unauthenticated_user
def connecter(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.info(request, 'Email et ou mot de passe incorrect !!!')

    context = {}
    return render(request, 'auth/login.html', context)

def deconnecter(request):
    
    logout(request)
    messages.info(request, 'User logout successfuly !!!')

    return redirect('connecter')


# LES VUES ADMIN

@droits_utilisateur(droit_acces=['admin'])
@login_required(login_url='connecter')
def acceuil(request):
       
    utilisateur = User.objects.filter(groups__name='admin')

    context = {'utilisateur': utilisateur}
    return render(request, 'admin/acceuil.html', context)

@droits_utilisateur(droit_acces=['admin'])
@login_required(login_url='connecter')
def agentSancfis_page_admin(request):
       
    agentsancfis = AgentSancfis.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_sancfis')

    context = {'agentsancfis': agentsancfis, 'utilisateur': utilisateur}
    return render(request, 'admin/admin_systeme.html', context)

@droits_utilisateur(droit_acces=['admin'])
@login_required(login_url='connecter')
def assurance_page_admin(request):

    assurances = Assurance.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_assurance')

    agentassurance = AgentAssurance.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_assurance')
    
    context = {'agentassurance': agentassurance, 'utilisateur': utilisateur,
                'assurances': assurances, 'utilisateur1': utilisateur1}
    return render(request, 'admin/assurance.html', context)

@droits_utilisateur(droit_acces=['admin'])
@login_required(login_url='connecter')
def assure_page_admin(request):
    
    assures = Assure.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assure')

    employes = Employe.objects.all()
    
    context = {'assures': assures, 'employes': employes, 'utilisateur': utilisateur}
    return render(request, 'admin/assure.html', context)

@droits_utilisateur(droit_acces=['admin'])
@login_required(login_url='connecter')
def pharmacie_page_admin(request):

    pharmacies = Pharmacie.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_pharmacie')

    agentpharmacie = AgentPharmacie.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_pharmacie')
    
    context = {'agentpharmacie': agentpharmacie, 'utilisateur': utilisateur,
                'pharmacies': pharmacies, 'utilisateur1': utilisateur1}
    return render(request, 'admin/pharmacies.html', context)

@droits_utilisateur(droit_acces=['admin'])
@login_required(login_url='connecter')
def laboratoire_page_admin(request):

    laboratoires = Laboratoire.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_labo')

    agentlaboratoire = AgentLaboratoire.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_labo')
    
    context = {'agentlaboratoire': agentlaboratoire, 'utilisateur': utilisateur,
                'laboratoires': laboratoires, 'utilisateur1': utilisateur1}
    return render(request, 'admin/labo.html', context)

@droits_utilisateur(droit_acces=['admin'])
@login_required(login_url='connecter')
def centreSoins_page_admin(request):

    centredesoins = centreDeSoins.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_cs')

    agentcs = AgentCs.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_cs')
    
    context = {'agentcs': agentcs, 'utilisateur': utilisateur,
                'centredesoins': centredesoins, 'utilisateur1': utilisateur1}
    return render(request, 'admin/centresdesoins.html', context)

@droits_utilisateur(droit_acces=['admin'])
@login_required(login_url='connecter')
def souscripteur_page_admin(request):

    souscripteurs = Souscripteur.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_souscripteur')

    context = {'souscripteurs': souscripteurs, 'utilisateur': utilisateur}
    return render(request, 'admin/souscripteurs.html', context)


# LES VUES AGENTS SANCFIS

@droits_utilisateur(droit_acces=['groupe_agent_sancfis'])
@login_required(login_url='connecter')
def assure_page_sancfis(request):
    
    assures = Assure.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assure')

    employes = Employe.objects.all()
    
    context = {'assures': assures, 'employes': employes, 'utilisateur': utilisateur}
    return render(request, 'sancfis/assure.html', context)


@droits_utilisateur(droit_acces=['groupe_agent_sancfis'])
@login_required(login_url='connecter')
def pharmacie_page_sancfis(request):

    pharmacies = Pharmacie.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_pharmacie')

    agentpharmacie = AgentPharmacie.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_pharmacie')
    
    context = {'agentpharmacie': agentpharmacie, 'utilisateur': utilisateur,
                'pharmacies': pharmacies, 'utilisateur1': utilisateur1}
    return render(request, 'sancfis/pharmacies.html', context)

@droits_utilisateur(droit_acces=['groupe_agent_sancfis'])
@login_required(login_url='connecter')
def laboratoire_page_sancfis(request):

    laboratoires = Laboratoire.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_labo')

    agentlaboratoire = AgentLaboratoire.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_labo')
    
    context = {'agentlaboratoire': agentlaboratoire, 'utilisateur': utilisateur,
                'laboratoires': laboratoires, 'utilisateur1': utilisateur1}
    return render(request, 'sancfis/labo.html', context)

@droits_utilisateur(droit_acces=['groupe_agent_sancfis'])
@login_required(login_url='connecter')
def centreSoins_page_sancfis(request):

    centredesoins = centreDeSoins.objects.all()
    utilisateur1 = User.objects.filter(groups__name='groupe_cs')

    agentcs = AgentCs.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_cs')
    
    context = {'agentcs': agentcs, 'utilisateur': utilisateur,
                'centredesoins': centredesoins, 'utilisateur1': utilisateur1}
    return render(request, 'sancfis/centresdesoins.html', context)

@droits_utilisateur(droit_acces=['groupe_agent_sancfis'])
@login_required(login_url='connecter')
def souscripteur_page_sancfis(request):

    souscripteurs = Souscripteur.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_souscripteur')

    context = {'souscripteurs': souscripteurs, 'utilisateur': utilisateur}
    return render(request, 'sancfis/souscripteurs.html', context)

@droits_utilisateur(droit_acces=['groupe_agent_sancfis'])
@login_required(login_url='connecter')
def agentSancfis_page(request):

    assurances = Assurance.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assurance')

    context = {'assurances': assurances, 'utilisateur': utilisateur}
    return render(request, 'sancfis/agents_sancfis.html', context)

@droits_utilisateur(droit_acces=['admin'])
@login_required(login_url='connecter')
def creerAgentSancfis(request):

    form = agentSancfisForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = agentSancfisForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_agent_sancfis')
            util.groups.add(groupe)

            return redirect('/')


    context = {'form': form, 'form1': form1}
    return render(request, 'sancfis/agentSancfis_form.html', context)

@droits_utilisateur(droit_acces=['groupe_agent_sancfis', 'admin'])
@login_required(login_url='connecter')
def modifierAgentSancfis(request, pk):

    agentsancfis = AgentSancfis.objects.get(id=pk)
    form = agentSancfisForm(instance=agentsancfis)

    if request.method == "POST":
        form = agentSancfisForm(request.POST, instance=agentsancfis)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form}
    return render(request, 'sancfis/agentSancfis_form.html', context)

@droits_utilisateur(droit_acces=['admin'])
@login_required(login_url='connecter')
def supprimerAgentSancfis(request, pk):

    agentsancfis = AgentSancfis.objects.get(id=pk)
    if request.method == "POST":
        agentsancfis.delete()
        return redirect('/')

    context = {'item': agentsancfis}
    return render(request, 'sancfis/supprimerAgentSancfis_form.html', context)

# LES VUES ASSURANCE

@login_required(login_url='connecter')
@droits_utilisateur(droit_acces=['groupe_agent_sancfis'])
def assurance_page(request):

    agentassurance = AgentAssurance.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_assurance')
    
    context = {'agentassurance': agentassurance, 'utilisateur': utilisateur}
    return render(request, 'assurance/assurance.html', context)

@droits_utilisateur(droit_acces=['groupe_agent_sancfis'])
@login_required(login_url='connecter')
def creerAssurance(request):
    
    form = assuranceForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = assuranceForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_assurance')
            util.groups.add(groupe)

            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'assurance/assurance_form.html', context)


# LES VUES AGENTS ASSURANCE

@login_required(login_url='connecter')
@droits_utilisateur(droit_acces=['groupe_agent_assurance', 'admin'])
def agentAssurance_page(request):

    assures = Assure.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assure')
    
    context = {'assures': assures, 'utilisateur': utilisateur}
    return render(request, 'assurance/agents_assurance.html', context)

@droits_utilisateur(droit_acces=['groupe_assurance'])
@login_required(login_url='connecter')
def creerAgentAssurance(request):
    
    form = agentAssuranceForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = agentAssuranceForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_agent_assurance')
            util.groups.add(groupe)

            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'assurance/agentAssurance_form.html', context)

# LES VUES ASSURE

@login_required(login_url='connecter')
@droits_utilisateur(droit_acces=['groupe_assure', 'admin', 'groupe_agent_sancfis'])
def assure_page(request):
    
    context = {}
    return render(request, 'assure/assure.html', context)

@login_required(login_url='connecter')
def creerAssure(request):
    
    form = assureForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = assureForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_assure')
            util.groups.add(groupe)

            messages.success(request, 'Compte crée pour' + email)


            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'assure/assure_form.html', context)

# LES VUES PHARMACIES

@login_required(login_url='connecter')
@droits_utilisateur(droit_acces=['groupe_pharmacie', 'admin', 'groupe_agent_sancfis'])
def pharmacie_page(request):

    agentpharmacie = AgentPharmacie.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_pharmacie')
    
    context = {'agentpharmacie': agentpharmacie, 'utilisateur': utilisateur}
    return render(request, 'pharmacie/pharmacies.html', context)

@login_required(login_url='connecter')
def creerPharmacie(request):
    
    form = pharmacieForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = pharmacieForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_pharmacie')
            util.groups.add(groupe)

            messages.success(request, 'Compte crée pour' + email)


            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'pharmacie/pharmacie_form.html', context)

# LES VUES AGENTS PHARMACIES

@login_required(login_url='connecter')
@droits_utilisateur(droit_acces=['groupe_agent_pharmacie', 'admin', 'groupe_agent_sancfis'])
def agentPharmacie_page(request):

    assure = Assure.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assure')
    
    context = {'assure': assure, 'utilisateur': utilisateur}
    return render(request, 'pharmacie/agents_pharmacie.html', context)

@login_required(login_url='connecter')
def creerAgentPharmacie(request):
    
    form = agentPharmacieForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = agentPharmacieForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_agent_pharmacie')
            util.groups.add(groupe)

            messages.success(request, 'Compte crée pour' + email)


            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'pharmacie/agentPharmacie_form.html', context)

    
# LES VUES LABORATOIRES

@login_required(login_url='connecter')
@droits_utilisateur(droit_acces=['groupe_laboratoire', 'admin', 'groupe_agent_sancfis'])
def laboratoire_page(request):

    agentlaboratoire = AgentLaboratoire.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_labo')
    
    context = {'agentlaboratoire': agentlaboratoire, 'utilisateur': utilisateur}
    return render(request, 'labo/labo.html', context)

@login_required(login_url='connecter')
def creerLaboratoire(request):
    
    form = laboratoireForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = laboratoireForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_laboratoire')
            util.groups.add(groupe)

            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'labo/labo_form.html', context)

# LES VUES AGENTS LABORATOIRES

@login_required(login_url='connecter')
@droits_utilisateur(droit_acces=['groupe_agent_labo', 'admin'])
def agentLaboratoire_page(request):

    assures = Assure.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assure')
    
    context = {'assures': assures, 'utilisateur': utilisateur}
    return render(request, 'labo/agents_labo.html', context)

@login_required(login_url='connecter')
def creerAgentLaboratoire(request):
    
    form = agentLaboratoireForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = agentLaboratoireForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_agent_labo')
            util.groups.add(groupe)

            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'labo/agentLabo_form.html', context)


# LES VUES CENTRES DE SOINS

@login_required(login_url='connecter')
@droits_utilisateur(droit_acces=['groupe_agent_sancfis'])
def centreSoins_page(request):

    agentcs = AgentCs.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_agent_cs')
    
    context = {'agentcs': agentcs, 'utilisateur': utilisateur}
    return render(request, 'cs/centresdesoins.html', context)

@login_required(login_url='connecter')
def creerCentreSoins(request):
    
    form = csForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = csForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_cs')
            util.groups.add(groupe)

            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'cs/cs_form.html', context)

# LES VUES AGENTS CENTRES DE SOINS

@login_required(login_url='connecter')
@droits_utilisateur(droit_acces=['groupe_agent_cs', 'admin'])
def agentCs_page(request):

    assures = Assure.objects.all()
    utilisateur = User.objects.filter(groups__name='groupe_assure')
    
    context = {'assures': assures, 'utilisateur': utilisateur}
    return render(request, 'cs/agents_cs.html', context)

@login_required(login_url='connecter')
def creerAgentCs(request):
    
    form = agentCsForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = agentCsForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_agent_cs')
            util.groups.add(groupe)

            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'cs/agentCs_form.html', context)

# LES VUES SOUSCRIPTEURS

@login_required(login_url='connecter')
@droits_utilisateur(droit_acces=['goupe_souscripteur', 'admin'])
def souscripteur_page(request):

    assures = Assure.objects.all()
    employes = Employe.objects.all()
    
    context = {'assures': assures, 'employes': employes}
    return render(request, 'souscripteur/souscripteurs.html', context)

@login_required(login_url='connecter')
def creerSouscripteur(request):
    
    form = souscripteurForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = souscripteurForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            util = form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            groupe = Group.objects.get(name='groupe_souscripteur')
            util.groups.add(groupe)

            Souscripteur.objects.create(
                utilisateur=util
            )

            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'souscripteur/souscripteur_form.html', context)

# LES VUES EMPLOYES

@login_required(login_url='connecter')
def employe_page(request):
    
    context = {}
    return render(request, 'employe/employe.html', context)

@login_required(login_url='connecter')
def creerEmploye(request):
    
    form = employeForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = employeForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            form1.save()
            
            form.save()

            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'employe/employe_form.html', context)

