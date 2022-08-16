from django.contrib import admin
from django.urls import path, include
from assurance import *
from assurance import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    ### URLS authentification

    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),


    path('connecter/', views.connecter, name="connecter"),
    
    ### URLS des Pages de redirections

    path('', views.adminSyteme, name="admin_systeme"),

    path('agents_sancfis/', views.agentSancfis, name="agent_sancfis"),

    path('assurance/', views.assurance, name="assurance"),

    path('centre_soins/', views.centreSoins, name="centre_soins"),

    path('pharmacie/', views.pharmacie, name="pharmacie"),

    path('laboratoire/', views.laboratoire, name="laboratoire"),

    path('assure/', views.assure, name="assure"),

    path('souscripteur/', views.souscripteur, name="souscripteur"),

    path('agent_assurance/', views.agentAssurance, name="agent_assurance"),

    path('agent_cs/', views.agentCs, name="agent_cs"),

    path('agent_pharmacie/', views.agentPharmacie, name="agent_pharmacie"),

    path('agent_laboratoire/', views.agentLaboratoire, name="agent_laboratoire"),

    path('employe/', views.employe, name="employe"),

    ### URLS des Methodes

    # AGENTS SANCFIS

    path('creer_agent_sancfis/', views.creerAgentSancfis, name="creer_agent_sancfis"),
    path('modifier_agent_sancfis/<str:pk>/', views.modifierAgentSancfis, name="modifier_agent_sancfis"),
    path('supprimer_agent_sancfis/<str:pk>/', views.supprimerAgentSancfis, name="supprimer_agent_sancfis"),

    # AGENTS ASSURANCE

    path('creer_agent_assurance/', views.creerAgentAssurance, name="creer_agent_assurance"),
    path('modifier_agent_assurance/<str:pk>/', views.modifierAgentSancfis, name="modifier_agent_assurance"),
    path('supprimer_agent_assurance/<str:pk>/', views.supprimerAgentSancfis, name="supprimer_agent_assurance"),

    # AGENT CENTRES DE SOINS

    path('creer_agent_cs/', views.creerAgentCs, name="creer_agent_cs"),
    path('modifier_agent_cs/<str:pk>/', views.modifierAgentSancfis, name="modifier_agent_cs"),
    path('supprimer_agent_cs/<str:pk>/', views.supprimerAgentSancfis, name="supprimer_agent_cs"),

    # AGENTS PHARMACIES

    path('creer_agent_pharmacie/', views.creerAgentPharmacie, name="creer_agent_pharmacie"),
    path('modifier_agent_pharmacie/<str:pk>/', views.modifierAgentSancfis, name="modifier_agent_pharmacie"),
    path('supprimer_agent_pharmacie/<str:pk>/', views.supprimerAgentSancfis, name="supprimer_agent_pharmacie"),

    # AGENTS LABORATOIRES

    path('creer_agent_laboratoire/', views.creerAgentLaboratoire, name="creer_agent_laboratoire"),
    path('modifier_agent_laboratoire/<str:pk>/', views.modifierAgentSancfis, name="modifier_agent_laboratoire"),
    path('supprimer_agent_laboratoire/<str:pk>/', views.supprimerAgentSancfis, name="supprimer_agent_laboratoire"),

    # CENTRES DE SOINS

    path('creer_cs/', views.creerCentreSoins, name="creer_agent_cs"),
    path('modifier_agent_cs/<str:pk>/', views.modifierAgentSancfis, name="modifier_agent_cs"),
    path('supprimer_agent_cs/<str:pk>/', views.supprimerAgentSancfis, name="supprimer_agent_cs"),

    # ASSURANCES

    path('creer_assurance/', views.creerAssurance, name="creer_assurance"),
    path('modifier_assurance/<str:pk>/', views.modifierAgentSancfis, name="modifier_assurance"),
    path('supprimer_assurance/<str:pk>/', views.supprimerAgentSancfis, name="supprimer_assurance"),

    # PHARMACIES

    path('creer_pharmacie/', views.creerPharmacie, name="creer_pharmacie"),
    path('modifier_pharmacie/<str:pk>/', views.modifierAgentSancfis, name="modifier_pharmacie"),
    path('supprimer_pharmacie/<str:pk>/', views.supprimerAgentSancfis, name="supprimer_pharmacie"),

    # LABORATOIRES

    path('creer_laboratoire/', views.creerLaboratoire, name="creer_laboratoire"),
    path('modifier_laboratoire/<str:pk>/', views.modifierAgentSancfis, name="modifier_laboratoire"),
    path('supprimer_laboratoire/<str:pk>/', views.supprimerAgentSancfis, name="supprimer_laboratoire"),

    # ASSURES

    path('creer_assure/', views.creerAssure, name="creer_assure"),
    path('modifier_assure/<str:pk>/', views.modifierAgentSancfis, name="modifier_assure"),
    path('supprimer_assure/<str:pk>/', views.supprimerAgentSancfis, name="supprimer_assure"),

    # SOUSCRIPTEUR

    path('creer_souscripteur/', views.creerSouscripteur, name="creer_souscripteur"),
    path('modifier_souscripteur/<str:pk>/', views.modifierAgentSancfis, name="modifier_souscripteur"),
    path('supprimer_souscripteur/<str:pk>/', views.supprimerAgentSancfis, name="supprimer_souscripteur"),

    # EMPLOYES

    path('creer_employe/', views.creerEmploye, name="creer_employe"),
    path('modifier_employe/<str:pk>/', views.modifierAgentSancfis, name="modifier_employe"),
    path('supprimer_employe/<str:pk>/', views.supprimerAgentSancfis, name="supprimer_employe"),
]

