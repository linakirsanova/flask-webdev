import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app import create_app, db

@pytest.fixture(scope='module')
def new_app():
    # setup
    app = create_app('testing')
    assert 'data-test.sqlite' in app.config['SQLALCHEMY_DATABASE_URI']
    test_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    db.create_all()

    # testing begins
    yield test_client

    # teardown
    db.session.remove()
    db.drop_all()
    ctx.pop()