from .models import *
from ariadne import convert_kwargs_to_snake_case

def listOngoingGames_resolver(obj, info):
    try:
        games = [game.to_dict() for game in Game.query.all()]
        res = []
        for game in games:
            if game['finished'] == 0:
                res.append(game)
        print(res)
        payload = {
            "success": True,
            "games": res
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def listFinishedGames_resolver(obj, info):
    try:
        games = [game.to_dict() for game in Game.query.all()]
        res = []
        for game in games:
            if game['finished'] != 0:
                res.append(game)
        print(res)
        payload = {
            "success": True,
            "games": res
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getGameScoreboard_resolver(obj, info, id):
    try:
        sb = Scoreboard.query.get(id)
        payload = {
            "success": True,
            "scoreboard": sb.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Scoreboard matching {id} not found"]
        }
    return payload