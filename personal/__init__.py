from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


my_env_var = os.getenv('MY_ENV_VAR')
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://hvromtczbzsibl:8fe161f4ec7fa13418527862779859eccc556f3c7ca78726cb8f0519726ca024@ec2-52-54-212-232.compute-1.amazonaws.com:5432/d4tr3jqns7frbv'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']='shdtee33gddg6djjguigfffvd@ft'
db=SQLAlchemy(app)
migrate=Migrate(app,db)

bcrypt=Bcrypt(app)
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
# app.config['MAIL_USERNAME']=os.environ.get('SMTP_USERNAME')
# app.config['MAIL_PASSWORD']=os.environ.get('SMTP_PASSWORD')
app.config['MAIL_USERNAME']="collablland@gmail.com"
app.config['MAIL_PASSWORD']="Spinn221!"

# login_manager = LoginManager(app)
# login_manager.init_app(app)
# from . import app