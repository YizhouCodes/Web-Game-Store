from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from urllib.parse import urlencode
import json.scanner
from .models import Game, GeneralUser, PlayersGames
from hashlib import md5
import json, datetime, uuid

SECRET = "-mri43GwM1XA8otOwbyFxY9dVHgA"
PAYMENT_SERVICE_URL = "https://tilkkutakki.cs.aalto.fi/payments/pay"
WEBSITE_ADDRESS = "http://127.0.0.1:8000"

ongoing_payments = {}

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
    allGames = Game.objects.all()
    if "c" in request.GET:
        filterCategory = request.GET["c"]
        games = Game.objects.all().filter(category = filterCategory)
    elif "n" in request.GET:
        searchName = request.GET["n"]
        games = Game.objects.all().filter(title__startswith = searchName)
    else:
        games = Game.objects.all()
    categoryList = []
    for game in allGames:
        if game.category not in categoryList:
            categoryList.append(game.category)
    context = {'games': games, 'categories': categoryList}
    return render(request, 'index.html', context)

def page_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

def my_games(request):
    userGames = PlayersGames.objects.all().filter(playerId = request.user)
    context = {'games': userGames}
    return render(request, 'my_games.html', context)

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
            addingFailed = True

        return HttpResponse(json.dumps({"success": not addingFailed}))

@require_http_methods(["GET", "POST"])
@login_required(login_url='/accounts/login/')
def show_game(request, game_id, game_name):
    current_user = request.user
    if request.method == 'GET':

        price = 0.0

        try:
            price = Game.objects.get(pk=game_id).price
        except:
            #return render(request, 'no_such_game.html', context=ctx) TODO
            return HttpResponse("No such game")

        ctx = {
            "game_id": game_id,
            "game_name": game_name,
            "price": price,
            "is_player": current_user.is_player(),
            "player_has_this_game": False
        }

        try:
            pid = request.GET.get("pid")
            ref = request.GET.get("ref")
            result = request.GET.get("result")
            checksum = request.GET.get("checksum")

            checksumstr = f"pid={pid:s}&ref={ref:s}&result={result:s}&token={SECRET:s}"
            if checksum != md5(checksumstr.encode('utf-8')).hexdigest():
                return HttpResponseRedirect(WEBSITE_ADDRESS + f"/payment_error?pid={pid:s}")

            if not ongoing_payments[pid]:
                return HttpResponseRedirect(WEBSITE_ADDRESS + f"/payment_error?pid={pid:s}")

            # Player has just bought this game - mark it
            PlayersGames.objects.create(gameId=Game.objects.get(pk=game_id), playerId=current_user, score=0.0, gameState="")
        except Exception as e:
            pass

        # Check if player own this game
        try:
            game = PlayersGames.objects.get(gameId=Game.objects.get(pk=game_id), playerId=current_user)
            ctx["player_has_this_game"] = True
            ctx["score"] = game.score
            ctx["game_state"] = game.gameState
        except Exception as e:
            pass

        return render(request, 'show_game.html', context=ctx)
    elif request.method == 'POST':
        amount = 0.0
        try:
            amount = float(request.POST.get('price'))
        except:
            return HttpResponse(json.dumps({"success": False, "msg": "No price parameter"}))

        payment_id = str(uuid.uuid4())

        seller_id = "YXOizFdTRC1Qcm9qZWN0" # Test seller ID
        try:
            seller_id = GeneralUser.objects.get( id = Game.objects.get(pk=game_id).developer.id ).payment_info
        except:
            return HttpResponse(json.dumps({"success": False, "msg": "No such game"}))

        error_url = WEBSITE_ADDRESS + "/payment_error"
        success_url = WEBSITE_ADDRESS + f"/game/{game_id}/{game_name}"
        cancel_url = WEBSITE_ADDRESS + "/payment_cancelled"

        checksumstr = f"pid={payment_id:s}&sid={seller_id:s}&amount={amount:.2f}&token={SECRET:s}"
        checksum = md5(checksumstr.encode('utf-8')).hexdigest()

        try:
            query = urlencode({
                "pid": payment_id,
                "sid": seller_id,
                "amount": amount,
                "success_url": success_url,
                "cancel_url": cancel_url,
                "error_url": error_url,
                "checksum": checksum
            })
            
            ongoing_payments[payment_id] = True
            return HttpResponseRedirect(PAYMENT_SERVICE_URL + "?" + query)
        except:
            return HttpResponse(json.dumps({"success": False, "msg": "Cannot send request to the payment service"}))

@require_http_methods(["GET"])
@login_required(login_url='/accounts/login/')
def show_payment_error(request):
    ctx = {
        "current_username": request.user.username
    }
    del ongoing_payments[ request.GET.get("pid") ]
    return render(request, 'payment_error.html', context=ctx)

@require_http_methods(["GET"])
@login_required(login_url='/accounts/login/')
def show_payment_cancel(request):
    ctx = {
        "current_username": request.user.username
    }
    del ongoing_payments[ request.GET.get("pid") ]
    return render(request, 'payment_cancel.html', context=ctx)
