from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
import json

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
