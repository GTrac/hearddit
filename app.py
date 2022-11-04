from flask import Flask, redirect, render_template, request
from models import db, users, subh, posts

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:HeardditAdminPassword@winhost:5432/hearddit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

new_user = users(user_name='test', user_password='test_password')

@app.get('/')
def index():
    return render_template('home_page.html')

@app.get('/login')
def index():
    return render_template('login.html')

@app.get('/home')
def index():
    return render_template('home_page.html')

@app.get('/login/create')
def index():
    return render_template('create_account.html')

@app.get('/create/post')
def index():
    return render_template('create_new_post.html')

