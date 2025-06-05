import os
from dotenv import load_dotenv

load_dotenv()
class ConfigProduction:
    DEBUG=False

class ConfigDevelopment:
    DEBUG=True

class ConfigTesting:
    TESTING=True