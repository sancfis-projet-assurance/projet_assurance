from django.shortcuts import render

# Create your views here.

def assurance(request):

    context = {}
    return render(request, 'assurance/assurance.html', context)