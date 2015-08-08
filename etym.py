# -*- coding: utf-8 -*-

import os
import re
import time
import sqlite3
from unicodedata import normalize
from flask import g, Flask, request, make_response, jsonify
from flask import render_template
from flask import redirect, url_for

app = Flask(__name__)
is_prod = 'heroku' in os.environ.get('PYTHONHOME', '')

app.debug = not is_prod

# Constants
DATABASE = "etym.db" if is_prod else "etym-dev.db"
SLUGPUNCT = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


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
        sql = "SELECT * FROM word WHERE word LIKE ? OR slug LIKE ? OR id = ?"
        etym = query_db(sql, [word]*3, one=True)
    return etym


def get_related(word_id, derivation_type=None):
    sql = """SELECT relation.connection_type,
          word.slug, word.id, word.word FROM relation
          LEFT JOIN word ON word.id = target_word_id
          WHERE source_word_id = ?"""
    args = [word_id]
    if derivation_type:
        sql += "AND connection_type = ?"
        args += [derivation_type]
    return query_db(sql, args)

def action_page(action):
    etym = get_word(request.args.get('word'))
    return render_template('action.html', word=etym,
                            action=action)


# Views
@app.route('/<word>')
def word(word=None):
    etym = get_word(word)
    if not etym:
        return make_response(render_template('404.html', word=word), 404)

    related = lambda rel_type: get_related(etym['id'], rel_type)
    diveration = {
        "to": related(1),
        "from": related(2)
    }
    return render_template('index.html', word=etym, diveration=diveration)


@app.route('/random')
def random():
    etym = get_word()
    return redirect(url_for('word', word=etym['slug']))


@app.route('/api')
@app.route('/api/<word>')
def api(word=None):
    etym = get_word(word)
    if not etym:
        return jsonify({"word": False})

    result = {
        "id": etym['id'],
        "type": etym['type'],
        "word": etym['word'],
        "description": etym['description'],
        "slug": etym['slug'],
        "origin": {
            "language": etym['origin'],
            "code": etym['origin_code'],
            "word": etym['original_word']
        },
        "diveration": {
            "to": [],
            "from": []
        }
    }

    related = get_related(etym['id'])
    for related_word in related:
        word = dict(related_word)
        path = 'to' if word['connection_type'] == 1 else 'from'
        word.pop('connection_type', None)
        result['diveration'][path] += [word]

    return jsonify(result)


@app.route('/about')
@app.route('/humans.txt')
def about():
    date = time.ctime(os.path.getmtime(__file__))
    return render_plain('humans.txt', date=date)

base_repo = 'https://github.com/f/etym'

@app.route('/contribute')
def contribute():
    word = get_word(request.args.get('word'))
    if not word:
        return "Hatalı kelime."
    return redirect('{0}/issues/new?labels=enhancement&assignee=f&title=Geni%C5%9Flet%3A%20{1}&body={2}'.format(base_repo, word['word'], word['description']))

@app.route('/typo')
def typo():
    word = get_word(request.args.get('word'))
    if not word:
        return "Hatalı kelime."
    return redirect('{0}/issues/new?labels=bug&assignee=f&title=%C4%B0mla%20veya%20Bilgi%20Hatas%C4%B1%3A%20{1}&body={2}'.format(base_repo, word['word'], word['description']))

@app.route('/new')
def new():
    return redirect('{0}/blob/master/README.md'.format(base_repo))

@app.route('/request')
def request_():
    return redirect('{0}/issues/new?labels=enhancement&assignee=f&title=Yeni Kelime%3A%20{1}'.format(base_repo, request.args.get('word', '')))


@app.route('/')
def index():
    search = request.args.get('w') or request.args.get('word', None)
    return word(search)
