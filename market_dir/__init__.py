from typing import Callable

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class MySQLAlchemy(SQLAlchemy):
    Column: Callable  # Use the typing to tell the IDE what the type is.
    String: Callable
    Integer: Callable


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db1.db'+'?check_same_thread=False'
db = MySQLAlchemy(app)

# Importing modules and routes
from market_dir import models, routes
