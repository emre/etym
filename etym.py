import os
import sqlite3
from flask import g
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

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

# Views
@app.route('/<word>')
def word(word):
    return render_template('index.html', word=word)

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
    search = request.args.get('w') or request.args.get('word', 'hello');
    return word(search); 

