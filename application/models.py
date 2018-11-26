from application import db
from datetime import datetime



class User(db.Model):
	id_ = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(128), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.format(self.username)



class Post(db.Model):
	id_ = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	time_stamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id_'))

	def __repr__(self):
		return '<Post {}>'.format(self.body)
