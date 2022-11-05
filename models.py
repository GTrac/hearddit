from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), nullable=False)
    user_password = db.Column(db.String(255), nullable=False)

class subh(db.Model):
    sub_id = db.Column(db.Integer, primary_key=True)
    sub_name = db.Column(db.String(20), nullable=False)
    sub_post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=True)
    post = db.relationship('posts', backref='subs', lazy=True)
    sub_subscriber = db.Column(db.String(255), db.ForeignKey('users.user_id'), nullable=True)
    user = db.relationship('users', backref='subs', lazy=True)

class posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(255), nullable=False)
    post_link = db.Column(db.String(40000), nullable=True)
    post_text = db.Column(db.String(40000), nullable=True)
    post_title = db.Column(db.String(255), nullable=False)
    post_sub = db.Column(db.String(20), db.ForeignKey('subh.sub_id'), nullable=False)
    post_user = db.Column(db.String(20), db.ForeignKey('users.user_id'), nullable=False)
    user = db.relationship('users', backref='posts_made', lazy=True)