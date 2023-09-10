import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    '''
       
       Set config variables for the flask app
       using environment variables where available.
       Otherwise, create the config variableif not done already. 
    '''
    export FLASK_ENV=development
    export FLASK_APP=<NAME-OF-PROJECT>(ie drone_inventory)


SECRET_KEY = os.environ.get('SECRET_KEY') or 'Coding Temple Student Access'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///'+ os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_NOTIFICATIONS = False