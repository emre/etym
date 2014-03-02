import os
from flask import Flask
from flask import request
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

# Models
class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(80))
    original = db.Column(db.String(80))
    word_type = db.Column(db.String(40))
    data = db.Column(db.Text)
    create_date = db.Column(db.DateTime)

# Views
@app.route('/<word>')
def word(word):
    return render_template('index.html', word=word)

@app.route('/')
def index():
    search = request.args.get('w') or request.args.get('word', '');
    return word(search); 

