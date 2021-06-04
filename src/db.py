import configparser
import os
from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)

# Configuring Environment Variables

#config = configparser.ConfigParser()
#config.read('.env')
#PATH = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
#config.read(os.path.join(PATH, '.env'))

mysql = MySQL()

# Local DB Configuration
app.config['MYSQL_USER'] = root
app.config['MYSQL_PASSWORD'] = 
app.config['MYSQL_DB'] = FLAPI
app.config['MYSQL_CURSORCLASS'] = DictCursor

#app.config['MYSQL_HOST'] = 'localhost'

app.config['MYSQL_PORT'] = 3306

mysql.init_app(app)


# Init App

def db_connection():
    try:
        cursor = mysql.connection.cursor()
    except Exception as error:
        raise error
    return cursor
