from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from typing import Callable


class MySQLAlchemy(SQLAlchemy):
    Column: Callable  # Use the typing to tell the IDE what the type is.
    String: Callable
    Integer: Callable


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db1.db'
db = MySQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(length=1024), nullable=False)

    def __repr__(self):
        return f'Name: {self.name} \n Barcode: {self.barcode}, Price: {self.price} \n'


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/market')
def market():
    items = Item.query.all()
    return render_template('market.html', items=items)


# Default Route

@app.route('/<anything_else>')
def anything(anything_else=None):
    anything_else = ''.join(e for e in anything_else if e.isalnum() or e in "._")
    if len(anything_else) < 10:
        return render_template('default.html', anything_else=anything_else)
    else:
        return render_template('default.html', anything_else=anything_else[:9] + '...')
    # return f'<h2>\"{anything_else}\", Seriously !!</h2>'
