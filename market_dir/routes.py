from market_dir import app
from market_dir.models import Item
from flask import render_template


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
