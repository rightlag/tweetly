import flask
import logging
import os
import requests

from base64 import b64encode
from datetime import datetime
from functools import wraps
from twitter import app
from twitter import mysql

BASE_URL = 'https://api.twitter.com/1.1'


def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if 'access_token' not in flask.session:
            return authenticate()
        return fn(*args, **kwargs)
    return wrapper


def authenticate():
    """Obtain a bearer token."""
    url = 'https://api.twitter.com/oauth2/token'
    data = {
        'grant_type': 'client_credentials',
    }
    bearer = (
        '%s:%s' % (app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET'])
    ).encode('utf-8')
    encoded = b64encode(bearer)
    # `decode` method is required to convert byte stream to string.
    headers = {
        'Authorization': 'Basic %s' % encoded.decode(),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code not in range(200, 300):
        return flask.jsonify(response.json())
    access_token = response.json()['access_token']
    flask.session['access_token'] = access_token
    return flask.redirect('/')


@app.route('/fetch', methods=['POST'])
@login_required
def fetch():
    url = BASE_URL + '/statuses/user_timeline.json'
    params = flask.request.json
    # Authenticate API requests with the bearer token.
    access_token = flask.session['access_token']
    headers = {
        'Authorization': 'Bearer %s' % access_token,
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code not in range(200, 300):
        return flask.jsonify(response.json()), response.status_code
    # Persist the response object to the database.
    content = response.json()[0]
    handle = content['user']['screen_name']
    tweet = content['text']
    fetched = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        cursor = mysql.connection.cursor()
        query = '''
            INSERT INTO tweets (handle, tweet, fetched)
            VALUES ("%s", "%s", "%s")
        ''' % (handle, tweet, fetched)
        cursor.execute(query)
        mysql.connection.commit()
    except Exception as e:
        logging.error(e.args[1])
    return flask.jsonify(response.json())


@app.route('/')
@login_required
def hello():
    return flask.render_template('feed.html')

app.secret_key = os.urandom(24)
