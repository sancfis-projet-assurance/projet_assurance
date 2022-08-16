from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group
from assurance.forms import *
from assurance.models import *
from .privileges import *

# AUTHENTIFICATION

def connecter(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('mdp')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_systeme')
        else:
            messages.info(request, 'Email et ou mot de passe incorrect !!!')

    context = {}
    return render(request, 'auth/login.html', context)


# LES VUES ADMIN

@droits_admin
@login_required(login_url='login')
def adminSyteme(request):
       
    agentsancfis = AgentSancfis.objects.all()
    utilisateur = User.objects.all()

    context = {'agentsancfis': agentsancfis, 'utilisateur': utilisateur}
    return render(request, 'admin/admin_systeme.html', context)

# LES VUES AGENTS SANCFIS

@droits_utilisateur_type1(droit_agent_sancfis=['groupe_agent_sancfis', 'admin'])
@login_required(login_url='login')
def agentSancfis(request):

    assurances = Assurance.objects.all()
    utilisateur = User.objects.all()

    context = {'assurances': assurances, 'utilisateur': utilisateur}
    return render(request, 'sancfis/agents_sancfis.html', context)

@login_required(login_url='login')
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

            messages.success(request, 'Compte crée pour' + email)

            return redirect('/')


    context = {'form': form, 'form1': form1}
    return render(request, 'sancfis/agentSancfis_form.html', context)

@login_required(login_url='login')
def modifierAgentSancfis(request, pk):

    agentsancfis = agentSancfis.objects.get(id=pk)
    form = agentSancfisForm(instance=agentsancfis)

    if request.method == "POST":
        form = agentSancfisForm(request.POST, instance=agentsancfis)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form}
    return render(request, 'sancfis/agentSancfis_form.html', context)

@login_required(login_url='login')
def supprimerAgentSancfis(request, pk):

    agentsancfis = AgentSancfis.objects.get(id=pk)
    if request.method == "POST":
        agentsancfis.delete()
        return redirect('/')

    context = {'item': agentsancfis}
    return render(request, 'sancfis/supprimerAgentSancfis_form.html', context)

# LES VUES ASSURANCE

@login_required(login_url='login')
@droits_utilisateur_type6(droit_assurance=['groupe_assurance', 'admin', 'groupe_agent_sancfis'])
def assurance(request):

    agentassurance = AgentAssurance.objects.all()
    utilisateur = User.objects.all()
    
    context = {'agentassurance': agentassurance, 'utilisateur': utilisateur}
    return render(request, 'assurance/assurance.html', context)

@login_required(login_url='login')
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

            messages.success(request, 'Compte crée pour' + email)

            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'assurance/assurance_form.html', context)


# LES VUES AGENTS ASSURANCE

@login_required(login_url='login')
@droits_utilisateur_type2(droit_agent_assurance=['groupe_agent_assurance', 'admin'])
def agentAssurance(request):

    assures = Assure.objects.all()
    utilisateur = User.objects.all()
    
    context = {'assures': assures, 'utilisateur': utilisateur}
    return render(request, 'assurance/agents_assurance.html', context)

@login_required(login_url='login')
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

            messages.success(request, 'Compte crée pour' + email)


            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'assurance/agentAssurance_form.html', context)

# LES VUES ASSURE

@login_required(login_url='login')
@droits_utilisateur_type7(droit_assure=['groupe_assure', 'admin', 'groupe_agent_sancfis'])
def assure(request):
    
    context = {}
    return render(request, 'assure/assure.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
@droits_utilisateur_type8(droit_pharmacie=['groupe_pharmacie', 'admin', 'groupe_agent_sancfis'])
def pharmacie(request):

    agentpharmacie = AgentPharmacie.objects.all()
    utilisateur = User.objects.all()
    
    context = {'agentparmacie': agentpharmacie, 'utilisateur': utilisateur}
    return render(request, 'pharmacie/pharmacies.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
@droits_utilisateur_type5(droit_agent_pharmacie=['groupe_agent_pharmacie', 'admin', 'groupe_agent_sancfis'])
def agentPharmacie(request):
    
    context = {}
    return render(request, 'pharmacie/agents_pharmacie.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
@droits_utilisateur_type9(droit_laboratoire=['groupe_laboratoire', 'admin', 'groupe_agent_sancfis'])
def laboratoire(request):

    agentlaboratoire = AgentLaboratoire.objects.all()
    utilisateur = User.objects.all()
    
    context = {'agentlaboratoire': agentlaboratoire, 'utilisateur': utilisateur}
    return render(request, 'labo/labo.html', context)

@login_required(login_url='login')
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

            messages.success(request, 'Compte crée pour' + email)


            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'labo/labo_form.html', context)

# LES VUES AGENTS LABORATOIRES

@login_required(login_url='login')
@droits_utilisateur_type3(droit_agent_labo=['groupe_agent_labo', 'admin'])
def agentLaboratoire(request):
    
    context = {}
    return render(request, 'labo/agents_labo.html', context)

@login_required(login_url='login')
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

            messages.success(request, 'Compte crée pour' + email)


            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'labo/agentLabo_form.html', context)


# LES VUES CENTRES DE SOINS

@login_required(login_url='login')
@droits_utilisateur_type10(droit_cs=['groupe_cs', 'admin', 'groupe_agent_sancfis'])
def centreSoins(request):

    agentcs = AgentCs.objects.all()
    utilisateur = User.objects.all()
    
    context = {'agentcs': agentcs, 'utilisateur': utilisateur}
    return render(request, 'cs/centresdesoins.html', context)

@login_required(login_url='login')
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

            messages.success(request, 'Compte crée pour' + email)


            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'cs/cs_form.html', context)

# LES VUES AGENTS CENTRES DE SOINS

@login_required(login_url='login')
@droits_utilisateur_type4(droit_agent_cs=['groupe_agent_cs', 'admin'])
def agentCs(request):
    
    context = {}
    return render(request, 'cs/agents_cs.html', context)

@login_required(login_url='login')
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

            messages.success(request, 'Compte crée pour' + email)


            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'cs/agentCs_form.html', context)

# LES VUES SOUSCRIPTEURS

@login_required(login_url='login')
@droits_utilisateur_type11(droit_souscripteur=['goupe_souscripteur', 'admin'])
def souscripteur(request):

    assure = Assure.objects.all()
    employe = Employe.objects.all()
    utilisateur = User.objects.all()
    
    context = {'assure': assure, 'employe': employe, 'utilisateur': utilisateur}
    return render(request, 'souscripteur/souscripteurs.html', context)

@login_required(login_url='login')
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

            messages.success(request, 'Compte crée pour' + email)


            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'souscripteur/souscripteur_form.html', context)

# LES VUES EMPLOYES

@login_required(login_url='login')
def employe(request):
    
    context = {}
    return render(request, 'employe/employes.html', context)

@login_required(login_url='login')
def creerEmploye(request):
    
    form = employeForm()
    form1 = creerUtillisateur()
    if request.method == "POST":
        form = employeForm(request.POST)
        form1 = creerUtillisateur(request.POST)


        if form.is_valid() and form1.is_valid():
            form1.save()
            
            form.save()

            email = form1.cleaned_data.get('email')

            return redirect('/')

    context = {'form': form, 'form1': form1}
    return render(request, 'employe/employe_form.html', context)

