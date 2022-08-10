from django.shortcuts import render
from assurance.models import agentsSancfis

def adminSyteme(request):
    
    agentsancfis = agentsSancfis.objects.all()

    context = {'agentsancfis': agentsancfis}
    return render(request, 'admin/admin_systeme.html', context)