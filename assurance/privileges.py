from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def droits_acces(view_func):
    def wrapper_func(request, *args, **kwargs):
    
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'groupe_assurance':
            return redirect('admin_systeme')

        if group == 'groupe_pharmacie':
            return redirect('admin_systeme')

        if group == 'groupe_cs':
            return redirect('admin_systeme')

        if group == 'groupe_labo':
            return redirect('admin_systeme')

        if group == 'groupe_agent_assurance':
            return redirect('admin_systeme')

        if group == 'groupe_agent_pharmacie':
            return redirect('admin_systeme')

        if group == 'groupe_agent_cs':
            return redirect('admin_systeme')

        if group == 'groupe_agent_labo':
            return redirect('admin_systeme')

        if group == 'groupe_agent_sancfis':
            return redirect('admin_systeme')

        if group == 'assure':
            return redirect('admin_systeme')

        if group == 'admin':
            return view_func(request, *args, **kwargs)
            
    return wrapper_func
