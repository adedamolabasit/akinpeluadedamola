from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] =''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']='shdtee33gddg6djjguigfffv@ft'
db=SQLAlchemy(app)
migrate=Migrate(app,db)

bcrypt=Bcrypt(app)
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
app.config['MAIL_USERNAME']="collablland@gmail.com"
app.config['MAIL_PASSWORD']="Spinn221!"
# login_manager = LoginManager(app)
# login_manager.init_app(app)
# from . import app