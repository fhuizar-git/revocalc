import os
#import sqlite3
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#db_path = os.path.join(BASE_DIR, "site.db")

class Config:
    """
    The Config class for the application.

    Manually configure attributes of the config attribute of the Flask object. These will
    later be added onto the actual config attribute.

    SECRET_KEY:                 Used for security,                                      :type str
    SQLALCHEMY_DATABASE_URI:    Determines name and place for database file.            :type str

    SQLALCHEMY_TRACK_MODIFICATIONS:     Used for suppressing a warning.                 :type boolean
    """

    # os.environ.get returns a string, so save the environment variables as plain text (not with '')

    # SECRET_KEY = 'a618c71bc7605c466bf47d817f843531'
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'

    uri = os.environ.get("DATABASE_URL")  # or other relevant config var if uri.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = uri.replace("postgres://", "postgresql://", 1)
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///'+db_path
    #sqlite3.connect(db_path)
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

#import os
#basedir = os.path.abspath(os.path.dirname(__file__))

#class Config(object):
    # ...
#    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#        'sqlite:///' + os.path.join(basedir, 'site.db')
#    SQLALCHEMY_TRACK_MODIFICATIONS = False