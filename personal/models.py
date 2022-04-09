from email import message
from pydoc import describe
from personal import app,db
import datetime





class Profile(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(25),nullable=True)
    describe=db.Column(db.Text,nullable=True)
    twitter_link=db.Column(db.Text,nullable=True)
    facebook_link=db.Column(db.Text,nullable=True)
    instagram_link=db.Column(db.Text,nullable=True)
    linkdin=db.Column(db.Text,nullable=True)
    picture=db.Column(db.Text,nullable=True)

    def __repr__(self):
        return self.name
class About(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    job_title=db.Column(db.String(25),nullable=True)
    birthday=db.Column(db.String(25),nullable=True)
    phone=db.Column(db.String(25),nullable=True)
    sex=db.Column(db.String(25),nullable=True)
    describe=db.Column(db.Text,nullable=True)
    city=db.Column(db.Text,nullable=True)
    website_url=db.Column(db.Text,nullable=True)
    email=db.Column(db.Text,nullable=True)
    degree=db.Column(db.Text,nullable=True)
    information=db.Column(db.Text,nullable=True)
    skills=db.relationship('Skills',cascade='all,delete',backref='about')

    def __repr__(self):
        return self.job_title

class Skills(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    skill=db.Column(db.String(45),nullable=True)
    value=db.Column(db.Integer,nullable=True)
    backend=db.Column(db.Boolean,default=True)
    about_id=db.Column(db.Integer,db.ForeignKey('about.id'),nullable=True)
    def __repr__(self):
        return self.skill


class Resume(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    education=db.Column(db.Boolean,default=False)
    work_experience=db.Column(db.Boolean,default=False)
    name=db.Column(db.Text,nullable=True)
    role=db.Column(db.Text,nullable=True)
    location=db.Column(db.Text,nullable=True)
    start_date=db.Column(db.DateTime,default=datetime.datetime.now)
    end_date=db.Column(db.DateTime,default=datetime.datetime.now)
    describe1=db.Column(db.Text,nullable=True)
    describe2=db.Column(db.Text,nullable=True)
    describe3=db.Column(db.Text,nullable=True)
    describe4=db.Column(db.Text,nullable=True)
    describe5=db.Column(db.Text,nullable=True)
    def __repr__(self):
        return self.company_name

class Project(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(32),nullable=True)
    note=db.Column(db.String(152),nullable=True)
    description=db.Column(db.Text,nullable=True)
    image_link=db.Column(db.Text,nullable=True)
    category=db.Column(db.String(32),nullable=True)
    client=db.Column(db.String(52),nullable=True)
    github_url=db.Column(db.Text,nullable=True)
    project_url=db.Column(db.Text,nullable=True)
    project_date=db.Column(db.DateTime,default=datetime.datetime.now)
    def __repr__(self):
        return self.title
class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(72),nullable=True)
    email=db.Column(db.String(72),nullable=True)
    text=db.Column(db.Text,nullable=True)
    message=db.Column(db.String(32),nullable=True)
    def __repr__(self):
        return self.name




