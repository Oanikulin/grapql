
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://wffnpdwa:RKxxdF_whs3xk4T_cMm8unUsxjSyxzrv@tiny.db.elephantsql.com/wffnpdwa"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'API'