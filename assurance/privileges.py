from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('acceuil')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def droits_utilisateur(droit_acces=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in droit_acces:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('login')
                
        return wrapper_func
    return decorator

def droits_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
    
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'admin':
            return view_func(request, *args, **kwargs)
        elif group == 'groupe_agent_sancfis':
            return redirect('acceuil_sancfis')
        # else:
        #    return redirect('login')
            
    return wrapper_func


def droits_groups(*groups):
    def inner(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):

            if request.user.groups.filter(name__in = groups).exists():
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Vous n\'etes pas autorisé à voir cette page !!!')
        return wrapper_func
    return inner