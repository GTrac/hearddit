from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(255), unique=True, nullable=False)
    user_password = db.Column(db.String(255), nullable=False)

    def __init__(self, user_name, user_email, user_password) -> None:
       self.user_name = user_name, 
       self.user_email = user_email, 
       self.user_password = user_password
       
class community(db.Model):
    __tablename__ = 'community'
    com_id = db.Column(db.Integer, primary_key=True)
    com_name = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    owner = db.relationship('users', backref='coms', lazy=True)
    com_total_users = db.Column(db.Integer, nullable=False)

class posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(50), nullable=False)
    post_link = db.Column(db.String(40000), nullable=True)
    post_text = db.Column(db.String(40000), nullable=True)
    post_rating = db.Column(db.Integer, nullable=False)
    com_id = db.Column(db.Integer, db.ForeignKey('community.com_id'),nullable=False)

    def __init__(self, post_title, post_link, post_text, post_rating, com_id) -> None:
        self.post_title = post_title
        self.post_link = post_link
        self.post_text = post_text
        self.post_rating = post_rating
        self.com_id = com_id
    
    # Added so I can use the class in post_repository.py
    def __repr__(self) -> str:
        return f'Post(post_id = {self.post_id}, post_title = {self.post_title}, post_link = {self.post_link}, post_text = {self.post_text}, post_rating = {self.post_rating})'

# Junction table for comments and flagged comments.
flagged_comments_table = db.Table(
    'flagged_comments',
    db.Column('comment_id', db.Integer, \
        db.ForeignKey('comments.comment_id'), primary_key=True),
   
    
)


class user_comments(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    poster = db.relationship('users', backref='comments', lazy=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    post = db.relationship('posts', backref='comments', lazy=True)
    reply_id = db.Column(db.Integer, nullable=False)
    flagged_comment = db.Column(db.Boolean, nullable=True, default=False)
    flag = db.relationship('comments_flag', backref='comments', lazy=True)
    comment_text = db.Column(db.String(40000), nullable=False)
    comment_rating = db.Column(db.Integer, nullable=False)

class flag_comments(db.Model):
    flagged_comment = db.Column(db.Boolean, nullable=True, default=False, primary_key=True)
    comment_id = db.Column(db.Integer, nullable=False)
    comment = db.relationship('comments', backref='flag_comments', lazy=True)
    
com_post = db.Table(
    'com_post',
    db.Column('com_id', db.Integer, \
        db.ForeignKey('community.com_id'), primary_key=True),
    db.Column('post_id', db.Integer, \
        db.ForeignKey('posts.post_id'), primary_key=True),
)

user_com = db.Table(
    'user_com',
    db.Column('com_id', db.Integer, \
        db.ForeignKey('community.com_id'), primary_key=True),
    db.Column('user_id', db.Integer, \
        db.ForeignKey('users.user_id'), primary_key=True),
)

user_com = db.Table(
    'mod_com',
    db.Column('com_id', db.Integer, \
        db.ForeignKey('community.com_id'), primary_key=True),
    db.Column('mod_id', db.Integer, \
        db.ForeignKey('users.user_id'), primary_key=True),
    db.Column('mod_rank', db.Integer, nullable=False),
)
