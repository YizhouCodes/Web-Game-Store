from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

@require_http_methods(["GET", "POST"])
#@login_required(login_url='/accounts/login/') # TODO to uncomment when user will be created
def edit_profile(request):
    if request.method == 'GET':
        ctx = { # TODO get logged user: current_user = request.user
            "current_username": "current-username-here",
            "is_developer": True,
            "current_payment_info": "vjreinvuierji834=",
            "updated": False,
        }

        has_been_updated_successfully = request.GET.get('updated')
        if has_been_updated_successfully:
            ctx["updated"] = True
            ctx["has_been_updated_successfully"] = has_been_updated_successfully
            
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
                return HttpResponseRedirect(".?updated=true")
            except:
                return HttpResponseRedirect(".?updated=false")
        else:
            pass # Not valid request, do nothing

