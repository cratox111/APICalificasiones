from flask import Flask
from dotenv import load_dotenv
import os


def create_app():
    load_dotenv()
    app = Flask(__name__)
    
    env = os.getenv('FLASK_ENV')

    if env == 'production':
        from config import ConfigProduction
        app.config.from_object(ConfigProduction)
    elif env == 'testing':
        from config import ConfigTesting
        app.config.from_object(ConfigTesting)
    else:
        from config import ConfigDevelopment
        app.config.from_object(ConfigDevelopment)

    return app