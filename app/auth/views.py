from flask import render_template, flash, redirect, url_for
from . import auth
from flask_login import logout_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
  return render_template('register.html')

@auth.route('/logout')
def logout():
    logout_user()
    flash("You've been logged out successfully")
    return redirect(url_for('main.index'))