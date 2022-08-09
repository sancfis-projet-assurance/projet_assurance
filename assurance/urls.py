from django.contrib import admin
from django.urls import path, include
from assurance.views import agents_sancfis, assurance, admin_systeme

urlpatterns = [
    path('', admin_systeme.adminSyteme, name="admin_systeme"),
    path('agents_sancfis/', agents_sancfis.agentSancfis, name="agents_sancfis"),
    path('assurance/', assurance.assurance, name="assurance"),
    path('creer_agent_sancfis/', agents_sancfis.creerAgentSancfis, name="creer_agent_sancfis"),
    path('modifier_agent_sancfis/<str:pk>/', agents_sancfis.modifierAgentSancfis, name="modifier_agent_sancfis"),
    path('supprimer_agent_sancfis/<str:pk>/', agents_sancfis.supprimerAgentSancfis, name="supprimer_agent_sancfis"),
]

