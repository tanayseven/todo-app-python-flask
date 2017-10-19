from todo_app.extensions import db


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))


class AdminModel(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(UserModel.id))
    user = db.relationship(UserModel)
    email = db.Column(db.String(128), unique=True)


class ListUserModel(db.Model):
    __tablename__ = 'list_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(UserModel.id))
    user = db.relationship(UserModel)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
