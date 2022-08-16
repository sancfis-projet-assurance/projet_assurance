from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('admin_systeme')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def droits_utilisateur_type1(droit_agent_sancfis=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in droit_agent_sancfis:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('agent_sancfis')
                
        return wrapper_func
    return decorator

def droits_utilisateur_type2(droit_agent_assurance=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in droit_agent_assurance:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('agents_assurance')
                
        return wrapper_func
    return decorator

def droits_utilisateur_type3(droit_agent_labo=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in droit_agent_labo:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('agent_laboratoire')
                
        return wrapper_func
    return decorator

def droits_utilisateur_type4(droit_agent_cs=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in droit_agent_cs:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('agent_cs')
                
        return wrapper_func
    return decorator

def droits_utilisateur_type5(droit_agent_pharmacie=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in droit_agent_pharmacie:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('agent_pharmacie')
                
        return wrapper_func
    return decorator

def droits_utilisateur_type6(droit_assurance=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in droit_assurance:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('assurance')
                
        return wrapper_func
    return decorator

def droits_utilisateur_type7(droit_assure=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in droit_assure:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('assure')
                
        return wrapper_func
    return decorator

def droits_utilisateur_type8(droit_pharmacie=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in droit_pharmacie:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('pharmacie')
                
        return wrapper_func
    return decorator

def droits_utilisateur_type9(droit_laboratoire=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in droit_laboratoire:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('laboratoire')
                
        return wrapper_func
    return decorator

def droits_utilisateur_type10(droit_cs=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in droit_cs:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('centre_soins')
                
        return wrapper_func
    return decorator

def droits_utilisateur_type11(droit_souscripteur=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in droit_souscripteur:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('souscripteur')
                
        return wrapper_func
    return decorator

    

def droits_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
    
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'groupe_assure':
            return redirect('assure')
        
        if group == 'groupe_souscripteur':
            return redirect('souscripteur')

        if group == 'groupe_pharmacie':
            return redirect('pharmacie')

        if group == 'groupe_cs':
            return redirect('centre_soins')

        if group == 'groupe_labo':
            return redirect('laboratoire')
        
        if group == 'groupe_assurance':
            return redirect('assurance')

        if group == 'groupe_agent_pharmacie':
            return redirect('agent_pharmacie')

        if group == 'groupe_agent_cs':
            return redirect('agent_cs')

        if group == 'groupe_agent_labo':
            return redirect('agent_laboratoire')

        if group == 'groupe_agent_assurance':
            return redirect('agent_assurance')

        if group == 'groupe_agent_sancfis':
            return redirect('agent_sancfis')

        elif group == 'admin':
            return view_func(request, *args, **kwargs)
        
        else:
            return HttpResponse("Vous n'avez pas accès à cette page !!!")

            
    return wrapper_func
