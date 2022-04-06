from personal import app,db





class Profile(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(25),nullable=True)
    twitter_link=db.Column(db.Text,nullable=True)
    facebook_link=db.Column(db.Text,nullable=True)
    instagram_link=db.Column(db.Text,nullable=True)
    linkdin=db.Column(db.Text,nullable=True)
    picture=db.Column(db.Text,nullable=True)

    def __repr__(self):
        return self.name

