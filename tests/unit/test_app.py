from app import create_app, db
from app.models import User
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

def test_app_creation():
    app = create_app('testing')
    assert app

def test_current_app():
    app = create_app('testing')
    app.app_context().push()
    assert current_app
    assert current_app.config['TESTING']

def test_database_insert(new_app):
    u = User(email='john@example.com', username='john')
    db.session.add(u)
    db.session.commit()

def test_user_password(new_app):
    u1 = User(email='victor@example.com', username='victor', password = 'corn')
    u2 = User(email='anna@example.com', username='anna', password = 'clown')
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()
    assert u1.password_hash
    assert check_password_hash(u1.password_hash, 'corn')
    assert not check_password_hash(u1.password_hash, 'flower')
    assert u1.password_hash != u2.password_hash