
from flask import Flask, redirect, render_template, request, abort, session
from flask_sqlalchemy import SQLAlchemy
from src.repositories.post_repository import post_repository_singleton
from models import db, users, subh, posts, comments


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:HeardditAdminPassword@localhost:5432/hearddit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

test_new_user = users(user_name='test', user_password='test_password')

@app.get('/')
def index():
#Edit once Database models are implemented
    all_posts = ''
    communities = ['h/TestCommunity1', 'h/TestCommunity2', 'h/TestCommunity3']
    return render_template('home_page.html', list_posts = True, posts = all_posts, communities = communities)
    
@app.get('/post')
def save():
    return render_template('savingposts.html')

@app.get('/login')
def index_two():
    return render_template('login.html')

@app.get('/home')
def index_three():
    return render_template('home_page.html')

@app.post('/signup')
def create_account():
   
    email = request.form.get('email_input')
    email_confirm = request.form.get('email_confirm')
    username = request.form.get('enter_username')
    pasword = request.form.get('enter_password')

    # Need an if statement to make sure both email variables are equal. If not, then it should not go to the database.
    if email != email_confirm:
        error_message = 'Emails did not match'
        return render_template('signup.html', error_message = error_message)

    # return render_template('create_account.html', email=email, email_confirm=email_confirm,username=username,password=password)
    return redirect('/home')

# Needed two separate functions for a post and get route.
@app.get('/signup')
def get_create_form():
    return render_template('signup.html')


@app.get('/create/post')
def get_create_post():
    # Return this here in the get route.
    return render_template('create_new_post.html')

@app.post('/create/post')
def create_post():
    # Use variables from database.
    post_id = request.form.get('post_id', 0, type=int)
    post_title = request.form.get('post_title', ' ')
    post_link = request.form.get('post_link', ' ')
    post_text = request.form.get('post_text', ' ')
    post_rating = request.form.get('post_rating', 0, type=int)
    if post_title == ' ' or post_text == ' ':
        abort(400)
    new_post = post_repository_singleton.create_post()
    return redirect("/post/<id>")

@app.get('/post/<id>')
def post_page(id):
    db.session.add(id)
    db.session.commit()
    return render_template('post_page.html')

@app.post('/delete/post')
def delete_post(post_id):
    db.query.session.get_or_404(post_id)
    db.query.delete(post_id)
    db.query.commit()

    return redirect('/')
