import os

from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['CONSUMER_KEY'] = os.environ['CONSUMER_KEY']
app.config['CONSUMER_SECRET'] = os.environ['CONSUMER_SECRET']
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
mysql = MySQL(app)

import twitter.views
