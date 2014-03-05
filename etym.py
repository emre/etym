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
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# Helpers
def render_plain(template, **context):
    response = make_response(render_template(template, **context))
    response.headers['Content-Type'] = 'text/plain'
    return response

# Views
@app.route('/<word>')
def word(word):
    if (word is None):
        random = query_db("SELECT * FROM word ORDER BY RANDOM() LIMIT 1", one=True)
        word_item = random
    else:
        word_item = query_db("SELECT * FROM word WHERE word = ?", [word], one=True)
        if (word_item is None):
            return make_response(render_template('404.html', word=word), 404)

    return render_template('index.html', word=word_item)

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
    search = request.args.get('w') or request.args.get('word', None);
    return word(search); 

