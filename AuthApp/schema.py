from AuthApp.models import User
from settings.extension import ma
from marshmallow.exceptions import ValidationError


# Create schemas for models
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    # Field names
    id = ma.auto_field()
    firstName = ma.auto_field('first_name')
    lastName = ma.auto_field('last_name')
    username = ma.auto_field('username')
    email = ma.auto_field('email')
    mobile = ma.auto_field('mobile')
    isActive = ma.auto_field('is_active')
    isVerify = ma.auto_field('is_verify')
    updatedOn = ma.auto_field('updated_on')

