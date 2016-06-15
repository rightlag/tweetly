from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'twitter'
mysql = MySQL(app)

import twitter.views
