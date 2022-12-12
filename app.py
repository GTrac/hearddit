
from flask import Flask, redirect, render_template, request, abort, session
from flask_sqlalchemy import SQLAlchemy
from src.models import db, users, subh, posts, comments, comments_flag
import os
from dotenv import load_dotenv
from secuirty import bcrypt

from blueprints.session_blueprint import router as session_router
load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = os.getenv('APP_SECRET_KEY')

db.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(session_router)

@app.get('/')
def index():
    #Edit once Database models are implemented
    if 'user' not in session:
        all_posts=''
        communities = ['h/TestCommunity1', 'h/TestCommunity2', 'h/TestCommunity3']
        return render_template('home_page.html', list_posts = True, posts = all_posts, communities = communities)
    else:
        username=session.get('user')['user_name']
        return render_template('user_home_page.html', username=username)


@app.get('/post')
def save():
    return render_template('savingposts.html')

@app.get('/home')
def index_three():
    return render_template('home_page.html')


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
    new_post = posts(post_title = post_title, post_link=post_link, post_id=post_id, post_rating=post_rating)
    db.session.add(new_post)
    db.session.commit()
    return redirect("/post/<id>")

@app.get('/post/<id>')
def post_page(id):
    post_page = posts.query.get(id)
    return render_template('post_page.html', post_page=post_page)

@app.post('/delete/post')
def delete_post(post_id):
    # Need to retrieve id, and then delete it.
    post_delete = posts.query.get(post_id)
    db.session.delete(post_delete)
    db.session.commit()

    return redirect('/')