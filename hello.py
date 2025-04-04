from flask import Flask, render_template, redirect, url_for, session, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "zs9QFQp*6NQqqJxsGn4@m29ZTd.2v4"
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app, db, render_as_batch=True)

class NameForm(FlaskForm):
  name = StringField("What is your name?", validators=[DataRequired()])
  submit = SubmitField("Submit")

class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), unique=True)
  users = db.relationship('User', backref='role', lazy='dynamic')
  def __repr__(self):
      return f"<Role {self.name}>"

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), unique=True, index=True)
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

  def __repr__(self):
      return f"<User {self.username}>"

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name_entered = form.name.data
        user = User.query.filter_by(username=name_entered).first()
        if user is None:
            user = User(username=name_entered)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = name_entered
        flash('Great! We hope you enjoy the community')
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template(
        'index.html',
        form=form,
        name=session.get('name'),
        known=session.get('known', False))


@app.route('/about')
def about():
    return """<p>My name is Angelina Filippova, I'm a London-based
      frontend developer with 8 years of experience in web-development.
      I'm a curious individual with a passion for technology and learning new things.</p>
      <br><p>I enjoy exploring the possibilities of AI and finding
      creative ways to use digital tools.</p>"""


@app.route('/favorite-songs')
def songs():
  html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Favorite Songs</title>
    </head>
    <body>
        <h2>My Favorite Songs</h2>
        <ul>
            <li><strong>Crazy</strong> by Gnarls Barkley</li>
            <li><strong>Rolling in the Deep</strong> by Adele</li>
            <li><strong>Take on Me</strong> by A-ha</li>
            <li><strong>505</strong> by Arctic Monkeys</li>
            <li><strong>Yeah Right</strong> by Joji</li>
            <li><strong>Often</strong> by The Weeknd</li>
        </ul>
    </body>
    </html>
    """
  return html

@app.route('/menu')
def menu():
  return """<p>Check out <a href="/about">my About page</a>!</p>
    <p>And a <a href="/favorite-songs"> list of my favorite songs</a>!</p>
  """

@app.route('/apps/years-to-100/<name>/<age>')
def years_to_100(name, age):
   return f"Hey, {name}! You have {100 - int(age)} years until 100"

@app.errorhandler(403)
def forbidden(e):
    error_title = "Forbidden"
    error_msg = "You shouldn't be here!"
    return render_template('error.html',
                           error_title=error_title,error_msg=error_msg), 403


@app.errorhandler(404)
def page_not_found(e):
    error_title = "Not Found"
    error_msg = "That page doesn't exist"
    return render_template('error.html',
                           error_title=error_title,error_msg=error_msg), 404


@app.errorhandler(500)
def internal_server_error(e):
    error_title = "Internal Server Error"
    error_msg = "Sorry, we seem to be experiencing some technical difficulties"
    return render_template("error.html",
                           error_title=error_title,
                           error_msg=error_msg), 500
