'''
The legitimate Senate server for sending spies information.
'''

from flask import Flask, Response, redirect, url_for, request, session, abort, g
from flask.ext.login import LoginManager, UserMixin, \
    login_required, login_user, logout_user
import os, sqlite3, hashlib

app = Flask(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'spies.db'),
    DEBUG=True,
    SECRET_KEY='dankmemes_69'
))

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# User model with just id (here id is username)
class User(UserMixin):

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return "%s" % (self.id)


# some protected url
@app.route('/')
@login_required
def home():
    '''
    Displays the name of the login and target of the logged in spy
    '''
    spy = get_spy(session['user_id'])
    return Response("Hello {}, your target is {}.".format(spy['full_name'], spy['target']))


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    '''
    Allows a spy to login during a session
    '''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            # hash the password
            hash_pass = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
            # grab the password hash from the database
            get_spy(username)['password']
            if hash_pass == get_spy(username)['password']:
                # id = username.split('user')[1]
                user = User(username)
                login_user(user)
                return redirect(request.args.get("next"))
            else:
                return abort(401)
        except:
            return abort(401)
    else:
        # Return the login form if a GET request
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User(userid)


def get_spy(name):
    """Returns the spy info for the spy with the given username from a database."""
    cur = get_db().cursor()
    query = 'SELECT * FROM spy WHERE  username=?'
    cur.execute(query, (name,))
    return dict(cur.fetchone())


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
    app.run()
