import os
from dotenv import load_dotenv

load_dotenv()
class ConfigProduction:
    DEBUG=False

class ConfigDevelopment:
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_SECRET_KEY=os.getenv('JWT_PASSWORD')

class ConfigTesting:
    TESTING=True