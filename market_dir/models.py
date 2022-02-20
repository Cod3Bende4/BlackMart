from market_dir import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    email_addr = db.Column(db.String(length=40), unique=True, nullable=False)
    hAsh3s = db.Column(db.String(length=64), nullable=False)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(length=1024), nullable=False)

    def __repr__(self):
        return f'Name: {self.name} \n Barcode: {self.barcode}, Price: {self.price} \n'
