import os
import time
import sqlite3
from flask import g, Flask, request, make_response
from flask import render_template, send_from_directory

app = Flask(__name__)

# Database
DATABASE = "etym.db"
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Helpers
def render_plain(template, **context):
    response = make_response(render_template(template, **context))
    response.headers['Content-Type'] = 'text/plain'
    return response

# Views
@app.route('/<word>')
def word(word):
    return render_template('index.html', word=word)

@app.route('/humans.txt')
def about():
    date = time.ctime(os.path.getmtime(__file__))
    return render_plain('humans.txt', date=date)

@app.route('/edit')
def edit():
    return "coming soon"

@app.route('/extend')
def extend():
    return "coming soon"

@app.route('/typo')
def typo():
    return "coming soon"

@app.route('/')
def index():
    # TODO: Database select
    search = request.args.get('w') or request.args.get('word', 'hello');
    return word(search); 

