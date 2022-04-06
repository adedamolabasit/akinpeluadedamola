from pydoc import describe
from personal import app,db





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
    about_id=db.Column(db.Integer,db.ForeignKey('about.id'),nullable=True)

    def __repr__(self):
        return self.skill



