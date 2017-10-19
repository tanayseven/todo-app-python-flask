import os

SECRET_KEY = '98rjwo38mrxo7ty3w497tx'


def load_config(app, env='dev'):
    db_location = os.path.abspath('app.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_location) \
        if env == 'dev' else 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['TESTING'] = True
