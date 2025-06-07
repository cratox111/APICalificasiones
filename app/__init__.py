from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    
    env = os.getenv('FLASK_ENV')

    if env == 'production':
        from app.config import ConfigProduction
        app.config.from_object(ConfigProduction)
    elif env == 'testing':
        from app.config import ConfigTesting
        app.config.from_object(ConfigTesting)
    else:
        from app.config import ConfigDevelopment
        app.config.from_object(ConfigDevelopment)

    db.init_app(app)
    migrate.init_app(app, db)

    return app