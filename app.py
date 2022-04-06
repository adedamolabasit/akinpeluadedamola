from personal import app,db
from flask import render_template
from personal.models import *
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin




admin=Admin(app,template_mode='bootstrap3',name='Adedamola Akinpelu')

class Controllers(ModelView):
    pass
    # def is_accessible(self):

    #     if current_user.is_active:
    #         if current_user.permission is True:
    #             return current_user.is_authenticated 
    #         else:
    #             abort(403)           
    #     else: 
    #         abort(403)
    
   
 

    # def not_auth(self):
    #     return " you are not authorized to use the Nautilus dashboard "

admin.add_view(Controllers(Profile,db.session,name='Profile'))
admin.add_view(Controllers(About,db.session,name='About me'))






@app.route('/')
def index():
    query=Profile.query.filter_by(id=1).first()
    about=About.query.filter_by(id=1).first()
    return render_template('index.html',query=query,about=about)