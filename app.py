import os
from flask import Flask
from extensions import db
from routes import enregistrer_routes
import os

def creer_app():
    app = Flask(__name__)
    #basedir = os.path.abspath(os.path.dirname(__file__))
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users_groups.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    #app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://bdd_users_user:Rou60uFLUKhvFt9OWvKyxQEDdCeIQHNh@dpg-ct6mtdg8fa8c73cge6d0-a.oregon-postgres.render.com/bdd_users"

    #postgresql://bdd_users_user:Rou60uFLUKhvFt9OWvKyxQEDdCeIQHNh@dpg-ct6mtdg8fa8c73cge6d0-a.oregon-postgres.render.com/bdd_users
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    enregistrer_routes(app)
    return app