from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Game, GeneralUser, PlayersGames
import json

@require_http_methods(["POST"])
@login_required()
def post_score(request, game_id, game_name):
    try:
        pg = PlayersGames.objects.get(gameId=Game.objects.get(pk=game_id), playerId=request.user)
        new_score = float(request.POST.get('score'))
        if pg.score < new_score:
            pg.score = new_score
            pg.save()
        return HttpResponse(json.dumps({"status": True}).encode("utf8"))
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"status": False, "info": "Cannot save the score!"}).encode("utf8"))

    return HttpResponse(json.dumps({"status": False, "info": "Unknown error"}).encode("utf8"))

@require_http_methods(["POST"])
@login_required()
def save_state(request, game_id, game_name):
    try:
        pg = PlayersGames.objects.get(gameId=Game.objects.get(pk=game_id), playerId=request.user)

        game_state = {}
        if pg.gameState != "":
            game_state = json.loads(pg.gameState)
        game_state["gameState"] = json.loads(request.body.decode('utf-8'))
        pg.gameState = json.dumps(game_state)

        pg.save()
        return HttpResponse(json.dumps({"status": True}).encode("utf8"))
    except:
        return HttpResponse(json.dumps({"status": False, "info": "Cannot save the state!"}).encode("utf8"))

    return HttpResponse(json.dumps({"status": False, "info": "Unknown error"}).encode("utf8"))

@require_http_methods(["GET"])
@login_required()
def get_state(request, game_id, game_name):
    try:
        pg = PlayersGames.objects.get(gameId=Game.objects.get(pk=game_id), playerId=request.user)
        game_state = json.loads(pg.gameState)
        return HttpResponse(json.dumps({"status": True, "gameState": game_state["gameState"]}).encode("utf8"))
    except Exception as e:
        print(str(e))
        return HttpResponse(json.dumps({"status": False, "info": "Cannot return the state!"}).encode("utf8"))

    return HttpResponse(json.dumps({"status": False, "info": "Unknown error"}).encode("utf8"))

@require_http_methods(["POST"])
@login_required()
def post_settings(request, game_id, game_name):
    try:
        pg = PlayersGames.objects.get(gameId=Game.objects.get(pk=game_id), playerId=request.user)

        game_state = {}
        if pg.gameState != "":
            game_state = json.loads(pg.gameState)
        game_state["options"] = json.loads(request.body.decode('utf-8'))
        pg.gameState = json.dumps(game_state)
        
        pg.save()
        return HttpResponse(json.dumps({"status": True}).encode("utf8"))
    except Exception as e:
        return HttpResponse(json.dumps({"status": False, "info": "Cannot save the settings!"}).encode("utf8"))

    return HttpResponse(json.dumps({"status": False, "info": "Unknown error"}).encode("utf8"))