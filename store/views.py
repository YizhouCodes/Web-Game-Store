from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Game
import json, datetime

@require_http_methods(["GET", "POST"])
#@login_required(login_url='/accounts/login/') # TODO to uncomment when user will be created
def edit_profile(request):
    if request.method == 'GET':
        ctx = { # TODO get logged user: current_user = request.user
            "current_username": "current-username-here",
            "is_developer": True,
            "current_payment_info": "vjreinvuierji834=",
        }

        return render(request, 'edit_profile.html', context=ctx)
    elif request.method == 'POST':
        usr_name = request.POST.get('usrName')
        if usr_name:
            payment_info = request.POST.get('paymentInfo')
            if payment_info:
                # TODO Update developer
                # current_user.username = usr_name
                # current_user.payment_info = payment_info
                pass
            else:
                # TODO Update player
                # current_user.username = usr_name
                pass
            # TODO Commit update
            try:
                #current_user.save()
                return HttpResponse(json.dumps({"success": True}))
            except:
                return HttpResponse(json.dumps({"success": False}))
        else:
            # Not valid request, do nothing
            return HttpResponse(json.dumps({"success": False}))

def index(request):
    return render(request, 'index.html', {})

def page_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

@require_http_methods(["GET", "POST"])
@login_required(login_url='/accounts/login/')
def add_game(request):
    current_user = request.user
    if not current_user.is_developer():
        return render(request, 'you_are_not_developer.html')

    if request.method == 'GET':

        ctx = {
            "current_username": current_user.username
        }

        return render(request, 'add_game.html', context=ctx)
    elif request.method == 'POST':
        title = request.POST.get('gameTitle')
        desc = request.POST.get('gameDescription')
        screenshots = request.POST.get('screenshot')
        category = request.POST.get('gameCategory')
        minAge = request.POST.get('minAge')
        price = request.POST.get('price')
        gameUrl = request.POST.get('gameUrl')

        addingFailed = False
        try:
            new_game = Game.objects.create(
                title = title,
                developer = current_user,
                description = desc,
                dateOfUpload = datetime.date.today(),
                screenshots = screenshots,
                averageRating = 0.0,
                category = category,
                price = price,
                minimumAge = minAge)

            if new_game == None:
                addingFailed = True
        except Exception as e:
            print(e)
            addingFailed = True

        return HttpResponse(json.dumps({"success": not addingFailed}))
