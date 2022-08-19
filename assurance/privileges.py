from django.http import HttpResponse
from django.shortcuts import redirect

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
                return redirect('connecter')
                
        return wrapper_func
    return decorator
    

def droits_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
    
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'admin':
            return view_func(request, *args, **kwargs)

        else:
           return redirect('connecter')
            
    return wrapper_func
