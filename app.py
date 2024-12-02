import os
from flask import Flask
from extensions import db
from routes import enregistrer_routes
import os

# ---- 1ère étape : Configuration de la base de données ----
def creer_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    #print(os.environ.get("DATABASE_URL"))

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://bdd_users_user:Rou60uFLUKhvFt9OWvKyxQEDdCeIQHNh@dpg-ct6mtdg8fa8c73cge6d0-a.oregon-postgres.render.com/bdd_users"
    # URL DE LA BDD POSTGRESQL
    # postgresql://bdd_users_user:Rou60uFLUKhvFt9OWvKyxQEDdCeIQHNh@dpg-ct6mtdg8fa8c73cge6d0-a.oregon-postgres.render.com/bdd_users
    # Nom utl : bdd_users_user
    # mdp : Rou60uFLUKhvFt9OWvKyxQEDdCeIQHNh
    # BDD : bdd_users
    # Host : dpg-ct6mtdg8fa8c73cge6d0-a.oregon-postgres.render.com

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    enregistrer_routes(app)
    return app