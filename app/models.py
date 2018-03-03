from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(db.Model):

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return self.check_password_hash(self.password_hash)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
