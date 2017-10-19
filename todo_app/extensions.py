import os
from functools import wraps

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import Signer, BadSignature

from todo_app.config import load_config, SECRET_KEY

app = Flask(__name__, template_folder='templates/', static_url_path='')

load_config(app, os.environ['TODO_APP'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)
signer = Signer(SECRET_KEY)


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization') or request.form.get('Authorization')
        if token:
            try:
                signer.unsign(token)
            except BadSignature:
                return jsonify(dict(message='Unauthorized request')), 401
            else:
                return func(*args, **kwargs)
        else:
            return jsonify(dict(message='Unauthorized request')), 401

    return decorated_function
