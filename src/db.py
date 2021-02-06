import configparser
from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)

# Configuring Environment Variables

config = configparser.ConfigParser()
config.read('.env')

mysql = MySQL()

# Local DB Configuration
app.config['MYSQL_USER'] = config['local']['user']
app.config['MYSQL_PASSWORD'] = config['local']['password']
app.config['MYSQL_DB'] = config['local']['database']
app.config['MYSQL_CURSORCLASS'] = config['local']['cursor']
#app.config['MYSQL_HOST']='0.0.0.0'
mysql.init_app(app)


### Heroku Configuration

# app.config['MYSQL_USER'] = config['heroku']['user']
# app.config['MYSQL_HOST'] = config['heroku']['host']
# app.config['MYSQL_PASSWORD'] = config['heroku']['password']
# app.config['MYSQL_DB'] = config['heroku']['database']
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Init App

def db_connection():
    try:
        cursor = mysql.connection.cursor()
    except Exception as error:
        raise error
    return cursor
