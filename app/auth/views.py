from flask import render_template, flash, redirect, url_for
from . import auth
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash
from .forms import LoginForm
from ..models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
     return redirect(url_for('main.index'))

  form = LoginForm()

  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and user.verify_password(form.password.data):
      login_user(user, remember=form.remember_me.data)
      flash('Login successful!', 'success')
      return redirect(url_for('main.index'))
  else:
    flash('Invalid email or password', 'error')

  return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
  return render_template('register.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out successfully")
    return redirect(url_for('main.index'))