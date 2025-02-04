from market import app, db
from market import bcrypt
app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    items = db.relationship('Item', backref='owned_user', lazy=True)
     
    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=25), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(length=1024), nullable=False)
    owner= db.Column(db.Integer(), db.ForeignKey('user.id'))
    
def __repr__(self):
    return f'Item{self.name}'

