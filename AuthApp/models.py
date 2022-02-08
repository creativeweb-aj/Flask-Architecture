from werkzeug.security import generate_password_hash

from settings.extension import db, timestamp  # Database Object SQLAlchemy


# Auth App Models
# User
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    mobile = db.Column(db.Integer, unique=True, nullable=True)
    password = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_verify = db.Column(db.Boolean, default=False, nullable=False)
    is_delete = db.Column(db.Boolean, default=False, nullable=True)
    created_on = db.Column(db.String(80), nullable=True)
    updated_on = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return 'User : %r' % self.username

    @staticmethod
    def createUser(data):
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        email = data['email']
        mobile = data['mobile']
        password = data['password']
        password = generate_password_hash(password)
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            mobile=mobile,
            password=password,
            created_on=timestamp,
            updated_on=timestamp
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def updateUser(ID, data):
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        mobile = data['mobile']
        user = User.query.filter_by(
            id=ID, is_active=True, is_verify=True, is_delete=False
        ).first()
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.mobile = mobile
        db.session.commit()
        return user

class EmailHandler(db.Model):
    __tablename__ = 'email_handler'
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