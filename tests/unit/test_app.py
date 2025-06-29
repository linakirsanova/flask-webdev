from app import create_app, db
from app.models import User
from flask import current_app

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