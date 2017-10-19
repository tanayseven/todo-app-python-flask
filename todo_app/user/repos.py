from todo_app.extensions import db
from todo_app.user.models import AdminModel, UserModel, ListUserModel


class UserRepo:
    model = UserModel
    db = db

    @classmethod
    def add_new_user(cls, user_name, password):
        new_user = cls.model()
        new_user.user_name = user_name
        new_user.password = password
        cls.db.session.add(new_user)
        cls.db.session.commit()
        return new_user


class AdminRepo:
    model = AdminModel
    db = db

    @classmethod
    def add_new_admin(cls, user_name, password, email):
        new_user = UserRepo.add_new_user(user_name, password)
        new_admin = cls.model()
        new_admin.user = new_user
        new_admin.email = email
        cls.db.session.add(new_admin)
        cls.db.session.commit()

    @classmethod
    def fetch_user_for(cls, user_name, password):
        return cls.db.session.query(cls.model).join(UserModel) \
            .filter(UserModel.user_name == user_name).filter(UserModel.password == password).one_or_none()


class ListUserRepo:
    model = ListUserModel
    db = db

    @classmethod
    def load_user_if_exists(cls, auth_token):
        id = int(auth_token.split('.')[0])
        return cls.db.session.query(cls.model).join(UserModel) \
            .filter(ListUserModel.id == id).one_or_none()

    @classmethod
    def add_new_user(cls, user_name, password, email, first_name, last_name):
        new_user = UserRepo.add_new_user(user_name, password)
        new_list_user = cls.model()
        new_list_user.user = new_user
        new_list_user.email = email
        new_list_user.first_name = first_name
        new_list_user.last_name = last_name
        cls.db.session.add(new_list_user)
        cls.db.session.commit()

    @classmethod
    def load_user_with_credentials(cls, user_name, password):
        return cls.db.session.query(cls.model).join(UserModel) \
            .filter(UserModel.user_name == user_name)\
            .filter(UserModel.password == password).one_or_none()


