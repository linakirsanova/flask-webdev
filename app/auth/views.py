from flask import render_template, flash, redirect, url_for, request
from . import auth
from flask_login import logout_user, login_user, login_required, current_user
from .forms import LoginForm, RegistrationForm
from ..models import User
from .. import db

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
      next = request.args.get('next')
      if next is None or not next.startswith('/'):
        next = url_for('main.index')
      return redirect(next)
  else:
    flash('Invalid email or password', 'error')
  return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
     return redirect(url_for('main.index'))

  form = RegistrationForm()

  if form.validate_on_submit():
    user = User(
      email=form.email.data,
      username=form.username.data,
      password=form.password.data
    )

    db.session.add(user)
    db.session.commit()

    flash('Registration successful! You can now login.', 'success')
    return redirect(url_for('auth.login'))

  return render_template('auth/register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out successfully")
    return redirect(url_for('main.index'))