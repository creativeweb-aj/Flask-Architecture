import datetime
from MainApp.AppSettings.extension import db  # Database Object SQLAlchemy


# Auth App Models
# User
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_verify = db.Column(db.Boolean, default=False, nullable=False)
    created_on = db.Column(db.String(80), nullable=True)
    updated_on = db.Column(db.String(80), nullable=True)
    is_delete = db.Column(db.Boolean, default=False, nullable=True)

    def __repr__(self):
        return 'User : %r' % self.username


# Email Handler
class EmailHandler(db.Model):
    __tablename__ = 'emailhandler'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=True)
    body = db.Column(db.String(200), nullable=True)
    uuid = db.Column(db.String(200), nullable=True)
    is_sent = db.Column(db.Boolean, default=False, nullable=False)
    is_expiry = db.Column(db.Boolean, default=False, nullable=False)
    is_verify = db.Column(db.Boolean, default=False, nullable=False)
    sent_on = db.Column(db.String(80), nullable=True)
    created_on = db.Column(db.String(80), nullable=True)
    updated_on = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return 'Email Handler : %r || %r' % self.id, self.user_id
