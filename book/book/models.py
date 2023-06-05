
from book import db
from datetime import datetime
from werkzeug.security import check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    status = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), default=datetime.now())
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True
    
class LogBook(db.Model):
    __tablename__ = 'log_book'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    variable_type = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), default=datetime.now())

   
class LogEntry(db.Model):
    __tablename__ = 'log_entry'
    id = db.Column(db.Integer, primary_key=True)
    logbook_id = db.Column(db.Integer, db.ForeignKey('log_book.id'), nullable=False)
    log_value = db.Column(db.String(), nullable=False)
    status = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), default=datetime.now())

   