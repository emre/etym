import os
import time
import sqlite3
from flask import g, Flask, request, make_response, jsonify
from flask import render_template
from flask import redirect, url_for

app = Flask(__name__)
is_prod = False  # 'heroku' in os.environ.get('PYTHONHOME', '')

app.debug = not is_prod

# Database
DATABASE = "etym.db" if is_prod else "etym-dev.db"

# note to reviewer: C/P from Flask doc.
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


# note to reviewer: C/P from Flask doc.
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# note to reviewer: C/P from Flask doc.
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


def get_word(word=None):
    if not word:
        etym = query_db("SELECT * FROM word ORDER BY RANDOM() LIMIT 1",
                        one=True)
    else:
        etym = query_db("SELECT * FROM word WHERE word = ?", [word], one=True)
    return etym


# Views
@app.route('/<word>')
def word(word):
    etym = get_word(word)
    if not etym:
        return make_response(render_template('404.html', word=word), 404)
    return render_template('index.html', word=etym)


@app.route('/random')
def random():
    etym = get_word()
    return redirect(url_for('word', word=etym['word']))


@app.route('/api')
@app.route('/api/<word>')
def api(word=None):
    etym = get_word(word)
    if not etym:
        return jsonify({"word": False})
    return jsonify(**etym)


@app.route('/about')
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


@app.route('/new')
def new():
    return "coming soon"


@app.route('/')
def index():
    search = request.args.get('w') or request.args.get('word', None)
    return word(search)
