from django.contrib import admin
from django.urls import path, include
from assurance import *
from assurance import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    ### URLS authentification

    path('logout/', views.deconnecter, name="logout"),


    path('connecter/', views.connecter, name="connecter"),
    
    ### URLS des Pages de redirections

    path('', views.acceuil, name="acceuil"),
    path('agents_sancfis_admin/', views.agentSancfis_page_admin, name="agent_sancfis_admin"),
    path('assurance_admin/', views.assurance_page_admin, name="assurance_admin"),
    path('centre_soins_admin/', views.centreSoins_page_admin, name="centre_soins_admin"),
    path('pharmacie_admin/', views.pharmacie_page_admin, name="pharmacie_admin"),
    path('laboratoire_admin/', views.laboratoire_page_admin, name="laboratoire_admin"),
    path('assure_admin/', views.assure_page_admin, name="assure_admin"),
    path('souscripteur_admin/', views.souscripteur_page_admin, name="souscripteur_admin"),



    path('agents_sancfis/', views.agentSancfis_page, name="agent_sancfis"),
    path('centre_soins_sancfis/', views.centreSoins_page_sancfis, name="centre_soins_sancfis"),
    path('pharmacie_sancfis/', views.pharmacie_page_sancfis, name="pharmacie_sancfis"),
    path('laboratoire_sancfis/', views.laboratoire_page_sancfis, name="laboratoire_sancfis"),
    path('assure_sancfis/', views.assure_page_sancfis, name="assure_sancfis"),
    path('souscripteur_sancfis/', views.souscripteur_page_sancfis, name="souscripteur_sancfis"),

    path('assurance/', views.assurance_page, name="assurance"),

    path('centre_soins/', views.centreSoins_page, name="centre_soins"),

    path('pharmacie/', views.pharmacie_page, name="pharmacie"),

    path('laboratoire/', views.laboratoire_page, name="laboratoire"),

    path('assure/', views.assure_page, name="assure"),

    path('souscripteur/', views.souscripteur_page, name="souscripteur"),

    path('agent_assurance/', views.agentAssurance_page, name="agent_assurance"),

    path('agent_cs/', views.agentCs_page, name="agent_cs"),

    path('agent_pharmacie/', views.agentPharmacie_page, name="agent_pharmacie"),

    path('agent_laboratoire/', views.agentLaboratoire_page, name="agent_laboratoire"),

    path('employe/', views.employe_page, name="employe"),

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

    path('creer_cs/', views.creerCentreSoins, name="creer_cs"),
    path('modifier_cs/<str:pk>/', views.modifierAgentSancfis, name="modifier_cs"),
    path('supprimer_cs/<str:pk>/', views.supprimerAgentSancfis, name="supprimer_cs"),

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

