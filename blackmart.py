from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)


class Item(db.Model):
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
]


@app.route('/market')
def market():
    return render_template('market.html', items=items)


# Default Route

@app.route('/<anything_else>')
def anything(anything_else=None):
    anything_else = ''.join(e for e in anything_else if e.isalnum() or e in "._")
    if len(anything_else) < 10:
        return render_template('anything_else.html', anything_else=anything_else)
    else:
        return render_template('anything_else.html', anything_else=anything_else[:9] + '...')
    # return f'<h2>\"{anything_else}\", Seriously !!</h2>'
