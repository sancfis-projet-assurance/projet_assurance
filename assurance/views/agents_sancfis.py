from django.shortcuts import render, redirect
from assurance.forms import agentsSancfisForm
from assurance.models import agentsSancfis

# Create your views here.

def agentSancfis(request):

    context = {}
    return render(request, 'assurance/agents_sancfis.html', context)

def creerAgentSancfis(request):

    form = agentsSancfisForm()    
    if request.method == "POST":
        form = agentsSancfisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'assurance/agentSancfis_form.html', context)

def modifierAgentSancfis(request, pk):

    agentsancfis = agentsSancfis.objects.get(id=pk)
    form = agentsSancfisForm(instance=agentsancfis)

    if request.method == "POST":
        form = agentsSancfisForm(request.POST, instance=agentsancfis)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form}
    return render(request, 'assurance/agentSancfis_form.html', context)

def supprimerAgentSancfis(request, pk):

    agentsancfis = agentsSancfis.objects.get(id=pk)
    if request.method == "POST":
        agentsancfis.delete()
        return redirect('/')

    context = {'item': agentsancfis}
    return render(request, 'assurance/supprimerAgentSancfis_form.html', context)


