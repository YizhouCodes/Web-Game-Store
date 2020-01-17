from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def register_player(request):
    if request.method == 'POST'
        playerForm = PlayerRegisterForm (request.POST)
        if playerForm.is_valid():
            playerForm.save()

            username = playerForm.cleaned_data.get('username')
            email = playerForm.cleaned_data.get('email')

            

def register_developer(request):
    return HttpResponse('Hello, World! Developer')
