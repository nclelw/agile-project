import os

# django has a settings.py file in level above the current app's main folder

basedir = os.path.abspath(os.path.dirname(__file__))

# "The config is actually a subclass of a dictionary and
#        can be modified just like any dictionary: "
#                --from http://flask.pocoo.org/docs/config/
#  The full list of config options are linked above
#  So to be different I will set debug to True here and simplify our run.py
class Config(object):
    DATABASE = "polls.db"
    SECRET_KEY = "my_secret_key_of_hiding"
    DEBUG = True
    CSRF_ENABLED = True
#USERNAME = "admin"
#PASSWORD = "admin"
#SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
