import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = "zs9QFQp*6NQqqJxsGn4@m29ZTd.2v4"
    SQLALCHEMY_DATABASE_URI =\
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # @staticmethod
    def init_app(app):
        pass

config = {'default': Config}
