from sqlalchemy import desc
from personal import app,db
from flask import redirect, render_template,request,url_for
from personal.models import *
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_mail import Message,Mail




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
admin.add_view(Controllers(Skills,db.session,name='skills'))
admin.add_view(Controllers(Resume,db.session,name='Resume'))
admin.add_view(Controllers(Project,db.session,name='My Projects'))
admin.add_view(Controllers(Service,db.session,name='My Services'))



mail=Mail(app)


@app.route('/')
def index():
    query=Profile.query.filter_by(id=1).first()
    about=About.query.filter_by(id=1).first()
    resume=Resume.query.order_by(desc(Resume.start_date)).all()
    project=Project.query.all()
    service=Service.query.all()
    return render_template('index.html',
    query=query,about=about,resumes=resume
    ,projects=project,services=service
    )
@app.route('/details/projects/<int:id>/')
def project_details(id):
    project=Project.query.filter_by(id=id).first()
    return render_template('project-details.html',project=project)

@app.route('/contact',methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name=request.form.get('name',None)
        email=request.form.get('email',None)
        text=request.form.get('text',None)
        message=request.form.get('message',None)
        contact=Contact(name=name,email=email,text=text,message=message)
        db.session.add(contact)
        db.session.commit()


        # msg = Message('Contact message',
        # sender='Akinpelu Adedamola',
        # recipients=['adedamolabasit09@gmail.com'])
        # msg.body=f'''
        # Name:{name}
        # email:{email}
        # text:{email}
        # message={message}         
        # '''
        # mail.send(msg)  
        # msg = Message('Submitted',
        # sender='Akinpelu Adedamola',
        # recipients=[email])
        # msg.body=f'''
        # Thanks for the message
        # '''
        # mail.send(msg)  
    else:
        return redirect(url_for('index'))
    return redirect(url_for('index'))
  




if __name__ == '__main__':
    app.run()