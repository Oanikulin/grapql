from app import db
#from sqlalchemy.dialects.postgresql import ARRAY

class Scoreboard(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.ARRAY(db.String))
    victory = db.Column(db.ARRAY(db.String))
    def to_dict(self):
        return {
            "id": self.id,
            "names" : self.names,
            "victory" : self.victory
        }

class Game(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    finished = db.Column(db.Integer)
    comments = db.Column(db.ARRAY(db.String))
    def to_dict(self):
        return {
            "id": self.id,
            "finished" : self.finished,
            "comments" : self.comments
        }