import os
BASE_DIR = os.path.abspath(os.path.dirname('App/database/tmp.db'))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SECRET_KEY='dev'