from todo_app.extensions import db
from todo_app.user.models import ListUserModel


class ToDoListModel(db.Model):
    __tablename__ = 'todo_list'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(ListUserModel.id))
    name = db.Column(db.String(64))


class ItemModel(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(256), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    todo_list_id = db.Column(db.Integer, db.ForeignKey(ToDoListModel.id))
    todo_list = db.relationship(ToDoListModel)
