from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Game, GeneralUser
from hashlib import md5
import json
import uuid
import requests

SECRET = "-mri43GwM1XA8otOwbyFxY9dVHgA"
PAYMENT_SERVICE_URL = "https://tilkkutakki.cs.aalto.fi/payments/pay"
WEBSITE_ADDRESS = "127.0.0.1:8000"

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

@require_http_methods(["GET", "POST"])
#@login_required(login_url='/accounts/login/') # TODO to uncomment when user will be created
def show_game(request, game_id, game_name):
    # current_user = request.user
    if request.method == 'POST':
        amount = 0.0
        try:
            amount = request.POST.get('price')
        except:
            return HttpResponse(json.dumps({"success": False, "msg": "No price parameter"}))

        payment_id = str(uuid.uuid4())

        seller_id = "YXOizFdTRC1Qcm9qZWN0" # Test seller ID
        # The final code should be:
        try:
            seller_id = GeneralUser.objects.get( id = Game.objects.get(pk=game_id).developer ).payment_info
        except expression as identifier:
            return HttpResponse(json.dumps({"success": False, "msg": "No such game"}))

        error_url = WEBSITE_ADDRESS + "/payment_error"
        success_url = WEBSITE_ADDRESS + f"/{game_id}/{game_name}"
        cancel_url = WEBSITE_ADDRESS + "/payment_cancelled"

        checksumstr = f"pid={payment_id:s}&sid={seller_id:s}&amount={amount:.2f}&token={SECRET:s}"
        checksum = md5(checksumstr.encode('utf-8')).hexdigest()

        try:
            r = request.post(PAYMENT_SERVICE_URL, params = {
                "pid": payment_id,
                "sid": seller_id,
                "amount": amount,
                "success_url": success_url,
                "cancel_url": cancel_url,
                "error_url": error_url,
                "checksum": checksum
            })

            if r.status_code == 200:
                return HttpResponse(json.dumps({"success": True}))
            else:
                return HttpResponse(json.dumps({"success": False, "msg": f"Payment service return status code {r.status_code}"}))
        except:
            return HttpResponse(json.dumps({"success": False, "msg": "Cannot send request to the payment service"}))

@require_http_methods(["GET"])
#@login_required(login_url='/accounts/login/') # TODO to uncomment when user will be created
def show_payment_error(request):
    ctx = {
        "current_username": "current-username-here" # request.user.username
    }
    return render(request, 'payment_error.html', context=ctx)

@require_http_methods(["GET"])
#@login_required(login_url='/accounts/login/') # TODO to uncomment when user will be created
def show_payment_cancel(request):
    ctx = {
        "current_username": "current-username-here" # request.user.username
    }
    return render(request, 'payment_cancel.html', context=ctx)