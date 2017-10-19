from flask import Blueprint, request, jsonify

from todo_app.user.repos import ListUserRepo
from todo_app.extensions import app

user_endpoints = Blueprint('user', __name__, url_prefix='/user')


@user_endpoints.route('/register/', methods=('POST',))
def register_user():
    try:
        ListUserRepo.add_new_user(
            user_name=request.json.get("user_name"),
            password=request.json.get("password"),
            email=request.json.get("email"),
            first_name=request.json.get("first_name"),
            last_name=request.json.get("last_name"),
        )
        return jsonify({}), 200
    except:
        return jsonify({'message': 'User already exists'}), 400


@user_endpoints.route('/login', methods=('POST',))
def login_user():
    pass


@user_endpoints.route('/all', methods=('GET',))
def all_todo_lists():
    return jsonify(dict(todo_lists=[]))


app.register_blueprint(user_endpoints)
