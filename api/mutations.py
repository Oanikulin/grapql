from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import *

@convert_kwargs_to_snake_case
def createOngoingGame_resolver(obj, info):
    try:
        game = Game(
            finished=0, comments=[]
        )
        print("game created", flush=True)
        db.session.add(game)
        db.session.commit()
        payload = {
            "success": True,
            "errors": ["None"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

@convert_kwargs_to_snake_case
def finishGame_resolver(obj, info, id, names, result):
    try:
        game = Game.query.get(id)
        if game:
            game.finished = 1
        score = Scoreboard(id=game.id, names=names, victory=result)
        db.session.add(game)
        db.session.add(score)
        db.session.commit()
        payload = {
            "success": True,
            "scoreboard": score.to_dict()
        }

    except AttributeError:
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }

    return payload

@convert_kwargs_to_snake_case
def addComment_resolver(obj, info, id, comment):
    try:
        game = Game.query.get(id)
        if (game):
            game.comments.append(comment)
        db.session.add(game)
        db.session.commit()
        payload = {
            "success": True,
            "errors": ["None"]
        }

    except AttributeError as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload