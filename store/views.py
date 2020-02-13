from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from urllib.parse import urlencode
import json.scanner
from .models import Game, GeneralUser, PlayersGames, Review
from hashlib import md5
import json, datetime, uuid
from .forms import signUpFormPlayer, signUpFormDeveloper
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


SECRET = "-mri43GwM1XA8otOwbyFxY9dVHgA"

# Other testing pair: seller id PcwrDFRlc3RTZWxsZXI=, secret ajkv4gfixxyaW5EjgTtDgRxj9eoA

PAYMENT_SERVICE_URL = "https://tilkkutakki.cs.aalto.fi/payments/pay"
WEBSITE_ADDRESS = "http://radiant-refuge-85599.herokuapp.com/"

ongoing_payments = {}

####################################################################################################
################################## REGISTER PLAYER AND DEVELOPER ###################################
####################################################################################################

def register(request):
    if request.method == 'POST':
        if(request.POST.get('date_of_birth')!= None):
            print("in if")
            form = signUpFormPlayer (request.POST)
            if form.is_valid():
                return sendMail(request,form,1)
            else:
                msg = form.errors.as_text()
        else:
            print("in else")
            form = signUpFormDeveloper (request.POST)
            if form.is_valid():
                return sendMail(request,form,2)
            else:
                msg = form.errors.as_text()
                return render(request, 'register.html', {'formPlayer': signUpFormPlayer(), 'formDeveloper' :signUpFormDeveloper(), 'errors':msg})

    return render(request, 'register.html', {'formPlayer': signUpFormPlayer(), 'formDeveloper' :signUpFormDeveloper()})

####################################################################################################
####################################### SEND MAIL TO USER ##########################################
####################################################################################################
def sendMail(request,form , type):

    print(type)
    user = form.save (commit = False)
    user.is_active = False
    user.user_type = type
    if (type == 2):
        user.date_of_birth = "1000-10-10"
    user.save()

    current_site = get_current_site(request)
    username = form.cleaned_data.get('username')

    email = form.cleaned_data.get('email')
    message = render_to_string('activate_mail.html', {
        'username': username,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token':account_activation_token.make_token(user),
    })

    wrappedMail = EmailMessage ("Activate your Account" , message , to = [email])
    wrappedMail.send()

    try:
        return HttpResponse(json.dumps({"success": True}))
    except:
        return HttpResponse(json.dumps({"success": False}))

####################################################################################################
####################################### ACTIVATE ACCOUNT  ##########################################
####################################################################################################

def activate(request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = GeneralUser.objects.get(id=uid)

        except(TypeError, ValueError, OverflowError, GeneralUser.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()

            return render(request, 'activate_account_result.html', {"success": True})
        else:
            return render(request, 'activate_account_result.html', {"success": False})

####################################################################################################
######################################### RESET PASSWORD  ##########################################
####################################################################################################

def password_recovery(request):
        if request.method == 'GET':
                return render(request, 'password_recovery.html')

        if request.method == 'POST':
            username = request.POST.get('username')
            #print(username)
            try:
                user = GeneralUser.objects.get(username=username)
                ##print(user.email)
            except :
                return HttpResponse(json.dumps({"success": False}))

            current_site = get_current_site(request)
            message = render_to_string('passwrod_recovery_mail.html', {
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token':account_activation_token.make_token(user),
            })

            wrappedMail = EmailMessage ("Reset Password" , message , to = [user.email])
            wrappedMail.send()

            try:
                return HttpResponse(json.dumps({"success": True}))
            except:
                return HttpResponse(json.dumps({"success": False}))

####################################################################################################
######################################### SET PASSWORD  ############################################
####################################################################################################

def reset(request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = GeneralUser.objects.get(id=uid)

        except(TypeError, ValueError, OverflowError, GeneralUser.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            return render(request, 'password_change.html', {"success": True})
        else:
            return render(request, 'password_change.html', {"success": False})


####################################################################################################
######################################### CHANGE PASSWORD DONE #####################################
####################################################################################################

def reset_done(request):
    if request.method == 'POST':
        password = request.POST.get('password_change')
        print(password)
        print(request.user)
    return render(request, 'password_change_done.html', {"success": False})


####################################################################################################
######################################### EDIT PROFILE  ############################################
####################################################################################################


@require_http_methods(["GET", "POST"])
@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'GET':
        ctx = {
            "current_username": current_user.username,
            "is_developer": current_user.is_developer(),
            "current_payment_info": current_user.payment_info,
        }

        return render(request, 'edit_profile.html', context=ctx)
    elif request.method == 'POST':
        usr_name = request.POST.get('usrName')
        if usr_name:
            payment_info = request.POST.get('paymentInfo')
            if payment_info:
                # Update developer
                current_user.username = usr_name
                current_user.payment_info = payment_info
            else:
                # Update player
                current_user.username = usr_name
            # Commit update
            try:
                current_user.save()
                return HttpResponse(json.dumps({"success": True}))
            except:
                return HttpResponse(json.dumps({"success": False}))
        else:
            # Not valid request, do nothing
            return HttpResponse(json.dumps({"success": False}))

@require_http_methods(["GET"])
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

@login_required(login_url='/accounts/login/')
def page_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

@login_required(login_url='/accounts/login/')
@require_http_methods(["GET"])
def my_games(request):
    if request.user.is_developer():
        userGames = Game.objects.all().filter(developer = request.user.id)
    else:
        userGames = [g.gameId for g in PlayersGames.objects.all().filter(playerId = request.user.id)]
    context = {'games': userGames, 'is_developer': request.user.is_developer()}
    return render(request, 'my_games.html', context)

@require_http_methods(["GET", "POST"])
@login_required(login_url='/accounts/login/')
def add_game(request):
    current_user = request.user
    if not current_user.is_developer():
        return render(request, 'you_are_not_developer.html')

    if request.method == 'GET':

        ctx = {
            "current_username": current_user.username,
            "add_or_edit": "Add"
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
                url = gameUrl,
                minimumAge = minAge)

            if new_game == None:
                addingFailed = True
        except Exception as e:
            addingFailed = True

        return HttpResponse(json.dumps({"success": not addingFailed}))

@require_http_methods(["GET", "POST"])
@login_required(login_url='/accounts/login/')
def edit_game(request, game_id, game_name):
    current_user = request.user
    if not current_user.is_developer():
        return render(request, 'you_are_not_developer.html')

    game_to_edit = None
    try:
        game_to_edit = Game.objects.get(pk=game_id)
    except:
        return render(request, 'no_such_game.html')

    if game_to_edit.developer != current_user:
        return render(request, 'no_such_game.html')

    if request.method == 'GET':

        ctx = {
            "current_username": current_user.username,
            "add_or_edit": "Edit",
            "game": game_to_edit
        }

        return render(request, 'add_game.html', context=ctx)
    elif request.method == 'POST':
        game_to_edit.title = request.POST.get('gameTitle')
        game_to_edit.description = request.POST.get('gameDescription')
        game_to_edit.screenshots = request.POST.get('screenshot')
        game_to_edit.category = request.POST.get('gameCategory')
        game_to_edit.minimumAge = int(request.POST.get('minAge'))
        game_to_edit.price = float(request.POST.get('price'))
        game_to_edit.url = request.POST.get('gameUrl')

        addingFailed = False
        try:
            game_to_edit.save()
        except Exception as e:
            addingFailed = True

        return HttpResponse(json.dumps({"success": not addingFailed}))


####################################################################################################
######################################### DELETE GAME  #############################################
####################################################################################################

@require_http_methods(["DELETE"])
@login_required(login_url='/accounts/login/')
def delete_game(request, game_id, game_name):

    game = Game.objects.get(pk = game_id)
    game.delete()
    return HttpResponse('deleted')

####################################################################################################
#########################################  MANGE GAME  #############################################
####################################################################################################


@require_http_methods(["POST"])
@login_required(login_url='/accounts/login/')
def manage_game(request, game_id, game_name):

    game = Game.objects.get(id = game_id)
    game.title = request.POST.get('gameTitle')
    game.desc = request.POST.get('gameDescription')
    game.screenshots = request.POST.get('screenshot')
    game.category = request.POST.get('gameCategory')
    game.minAge = request.POST.get('minAge')
    game.price = request.POST.get('price')
    game.gameUrl = request.POST.get('gameUrl')

    game.save()

####################################################################################################
#########################################   SHOW GAME  #############################################
####################################################################################################


@require_http_methods(["GET", "POST"])
@login_required(login_url='/accounts/login/')
def show_game(request, game_id, game_name):
    current_user = request.user

    if request.method == 'GET':

        price = 0.0
        screenshot_url = ""
        game_desc = ""
        upload_data = ""
        category = ""
        avg_rating = ""
        developer = ""
        purchases = 0
        try:
            g = Game.objects.get(pk=game_id)
            price = g.price
            screenshot_url = g.screenshots
            game_desc = g.description
            upload_data = g.dateOfUpload
            category = g.category
            avg_rating = g.averageRating
            developer = g.developer.username
            purchases = g.purchases

            # User is too young to play this game
            if datetime.timedelta(days=g.minimumAge*365) > (datetime.date.today() - current_user.date_of_birth):
                raise Exception()

        except Exception as e:
            print(e)
            return render(request, 'no_such_game.html')

        ctx = {
            "game_id": game_id,
            "game_name": game_name,
            "price": price,
            "is_player": current_user.is_player(),
            "player_has_this_game": False,
            "screenshot_url" : screenshot_url,
            "game_desc": game_desc,
            "category": category,
            "upload_date": upload_data,
            "avg_rating": avg_rating,
            "developer": developer,
            "purchases": purchases
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
            boughtGame = Game.objects.get(pk=game_id)
            boughtGame.purchases += 1
            boughtGame.moneyEarned += boughtGame.price
            boughtGame.save()
            PlayersGames.objects.create(gameId=boughtGame, playerId=current_user, score=0.0, gameState="")
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

        reviewList = Review.objects.all().filter(gameId = Game.objects.get(pk=game_id))
        ctx["reviews"] = reviewList
        return render(request, 'show_game.html', context=ctx)
    elif request.method == 'POST':
        amount = 0.0
        try:
            amount = float(request.POST.get('price'))
        except:
            return HttpResponse(json.dumps({"success": False, "msg": "No price parameter"}))

        if amount == 0:
            # Player has just bought this game - mark it
            boughtGame = Game.objects.get(pk=game_id)
            boughtGame.purchases += 1
            boughtGame.moneyEarned += boughtGame.price
            boughtGame.save()
            PlayersGames.objects.create(gameId=boughtGame, playerId=current_user, score=0.0, gameState="")
            return HttpResponseRedirect(WEBSITE_ADDRESS + "/accounts/my_games")

        payment_id = str(uuid.uuid4())

        seller_id = "YXOizFdTRC1Qcm9qZWN0" # Test seller ID
        try:
            seller_id = GeneralUser.objects.get( id = Game.objects.get(pk=game_id).developer.id ).payment_info
        except:
            return HttpResponse(json.dumps({"success": False, "msg": "No such game"}))

        error_url = WEBSITE_ADDRESS + "/payment_error"
        success_url = WEBSITE_ADDRESS + f"/game/{game_id}/{game_name}"
        cancel_url = WEBSITE_ADDRESS + "/payment_cancelled"

        amount_str = f"{amount:.2f}"
        checksumstr = f"pid={payment_id:s}&sid={seller_id:s}&amount={amount_str:s}&token={SECRET:s}"
        checksum = md5(checksumstr.encode('utf-8')).hexdigest()

        try:
            query = urlencode({
                "pid": payment_id,
                "sid": seller_id,
                "amount": amount_str,
                "success_url": success_url,
                "cancel_url": cancel_url,
                "error_url": error_url,
                "checksum": checksum
            })

            ongoing_payments[payment_id] = True
            return HttpResponseRedirect(PAYMENT_SERVICE_URL + "?" + query)
        except:
            return HttpResponse(json.dumps({"success": False, "msg": "Cannot send request to the payment service"}))

@require_http_methods(["POST"])
@login_required(login_url='/accounts/login/')
def add_review(request, game_id, game_name):
    reviewText = request.POST.get("reviewInput")
    reviewRating = request.POST.get("rating")
    currentGame = Game.objects.get(pk = game_id)
    Review.objects.create(gameId = currentGame, playerId = request.user, rating = reviewRating, description = reviewText)
    numberOfReviews = len(Review.objects.all().filter(gameId = game_id))
    currentGame.averageRating = (currentGame.averageRating + float(reviewRating)) / numberOfReviews
    currentGame.save()
    return redirect("/game/" + str(game_id) + "/" + game_name)

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

@require_http_methods(["GET"])
@login_required(login_url='/accounts/login/')
def play_game(request, game_id, game_name):
    current_user = request.user
    try:
        g = Game.objects.get(pk=game_id)

        # User is too young to play this game
        if datetime.timedelta(days=g.minimumAge*365) > (datetime.date.today() - current_user.date_of_birth):
            raise Exception()

        # Get 4 highest scores of this game
        highest_scores = PlayersGames.objects.filter(gameId=game_id).order_by("-score")[:4]
        highest_scores = [str(s.score) for s in highest_scores]
        no_highest_scores = len(highest_scores) <= 0

        ctx = {
            "game_url": g.url,
            "game_title": g.title,
            "no_highest_scores": no_highest_scores,
            "scores": highest_scores
        }
        return render(request, 'play_game.html', context=ctx)
    except Exception as e:
        print(e)
        return render(request, 'no_such_game.html')
