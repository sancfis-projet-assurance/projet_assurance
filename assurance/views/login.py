from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

def connecter(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username / password is incorrect !!!')

    context = {}
    return render(request, 'auth/login.html', context)