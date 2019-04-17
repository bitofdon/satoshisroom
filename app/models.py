from datetime import datetime
from app import db

#User model and its corresponding table defined
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    #relationship between User and Post model - ref: https://docs.sqlalchemy.org/en/13/orm/collections.html
    #provides the list of posts the User created
    posts = db.relationship('Post', backref='author', lazy='dynamic')
        #backref = relationship-side, adds author attribute to Post model - ex: posts.author (calls a user instance)
        #lazy = makes the 'posts' be a query instead of a list of posts

    def __repr__(self):
        return '<User {}>'.format(self.username)


#For blog posts - import datetime
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Record who the author is for blog post

    def __repr__(self):
        return '<Post {}>'.format(self.body)
