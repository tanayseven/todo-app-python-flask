from flask import render_template, request, redirect
from flask_admin import Admin, expose, BaseView

from todo_app.extensions import signer
from todo_app.user.repos import AdminRepo


class LoginView(BaseView):
    @expose('/', methods=('GET', 'POST',))
    @expose('login/', methods=('GET', 'POST',))
    def index(self):
        if request.method == 'POST':
            user = AdminRepo.fetch_user_for(user_name=request.form.get('loginUsername'),
                                            password=request.form.get('loginPassword'))
            if user:
                token = signer.sign(bytes(user.id))
                return render_template('admin_home.html', token=token)
            return render_template('login.html', message='Invalid Credentials')
        return redirect('/admin/')

    @expose('register/', methods=('GET', 'POST',))
    def register(self):
        if request.method == 'POST':
            AdminRepo.add_new_admin(user_name=request.form.get('registerUsername'),
                                    password=request.form.get('registerPassword'),
                                    email=request.form.get('registerEmail'))
            return render_template('login.html', message='Successfully created account')
        return render_template('register.html')


def register_admin(app):
    admin = Admin(name='Dashboard', base_template='login.html')
    admin.add_view(LoginView(name="Login", endpoint='user/'))
    admin.init_app(app)
