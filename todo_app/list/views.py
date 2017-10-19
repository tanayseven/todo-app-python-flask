from flask import Blueprint, jsonify
from todo_app.extensions import app, login_required
from todo_app.list.repos import ToDoListRepo
from todo_app.user.repos import ListUserRepo

todo_list_endpoints = Blueprint('todo_list', __name__, url_prefix='todo_list/')
app.register_blueprint(todo_list_endpoints)


@todo_list_endpoints.route('/all', methods=('GET',))
@login_required
def all_todo_lists():
    auth_token = ''
    user = ListUserRepo.load_user_if_exists(auth_token)
    lists = ToDoListRepo.load_all_lists_for_(user)
    return jsonify(dict(todo_list=lists)), 200
