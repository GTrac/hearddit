from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), nullable=False)
    user_password = db.Column(db.String(255), nullable=False)

class subh(db.Model):
    sub_id = db.Column(db.Integer, primary_key=True)
    sub_name = db.Column(db.String(20), nullable=False)
    sub_owner = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    owner = db.relationship('users', backref='subs', lazy=True)
    sub_total_users = db.Column(db.Integer, nullable=True)

class posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(255), nullable=False)
    post_link = db.Column(db.String(40000), nullable=True)
    post_text = db.Column(db.String(40000), nullable=True)
    post_rating = db.Column(db.Integer, nullable=False)

class comments(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    poster = db.relationship('users', backref='comments', lazy=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    post = db.relationship('posts', backref='comments', lazy=True)
    reply_id = db.Column(db.Integer, nullable=False)
    comment_text = db.Column(db.String(40000), nullable=False)
    comment_rating = db.Column(db.Integer, nullable=False)
    
sub_post = db.Table(
    'sub_post',
    db.Column('sub_id', db.Integer, \
        db.ForeignKey('subh.sub_id'), primary_key=True),
    db.Column('post_id', db.Integer, \
        db.ForeignKey('posts.post_id'), primary_key=True),
)

user_sub = db.Table(
    'user_sub',
    db.Column('sub_id', db.Integer, \
        db.ForeignKey('subh.sub_id'), primary_key=True),
    db.Column('user_id', db.Integer, \
        db.ForeignKey('users.user_id'), primary_key=True),
)

user_sub = db.Table(
    'mod_sub',
    db.Column('sub_id', db.Integer, \
        db.ForeignKey('subh.sub_id'), primary_key=True),
    db.Column('mod_id', db.Integer, \
        db.ForeignKey('users.user_id'), primary_key=True),
    db.Column('mod_rank', db.Integer, nullable=False),
)
