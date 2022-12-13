
from flask import Flask, redirect, render_template, request, abort, session
from flask_sqlalchemy import SQLAlchemy
from src.models import db, users, community, posts, comments
from src.repositories.community_repository import com_singleton
from src.repositories.post_repository import post_singleton
import os
from dotenv import load_dotenv
from secuirty import bcrypt

from blueprints.session_blueprint import router as session_router
load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.secret_key = os.getenv('APP_SECRET_KEY')

db.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(session_router)

@app.get('/')
def index():
    all_posts = post_singleton.get_all_posts()
    all_communities = com_singleton.get_all_coms()
    username = None
    #Edit once Database models are implemented
    if 'user' not in session:
        login = 'visible'
        logout = 'hidden'
        return render_template('home_page.html', list_posts = True, posts = all_posts, communities = all_communities)
    else:
        login = 'hidden'
        logout = 'visible'
        username=session.get('user')['user_name']
    
    return render_template('home_page.html',login=login, logout=logout, username=username, list_posts = True, posts = all_posts, communities = all_communities)


@app.get('/post')
def save():
    return render_template('savingposts.html')

@app.get('/home')
def index_three():
    return render_template('home_page.html')


@app.get('/create/post')
def get_create_post():
    # Return this here in the get route.
    all_communities = com_singleton.get_all_coms()  
    return render_template('create_post.html', communities=all_communities)

@app.post('/create/post')
def create_post():
    # Use variables from database.
    post_title = request.form.get("title")
    post_link = request.form.get("post_link")
    post_text = request.form.get("post_text")
    com_id = request.form.get("com_id")
    # username=session.get('user')['user_name']
    # user = users.query.filter(text(username))
    # user_id = user.id
    if post_title == ' ' or post_text == ' ':
        abort(400)
    new_post = posts(com_id=com_id, post_title=post_title, post_link=post_link, post_text=post_text, post_rating=1)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/post/{new_post.post_id}')

@app.get('/post/<int:post_id>')
def post_page(post_id):
    post_obj = posts.query.get(post_id)
    return render_template('card.html', post=post_obj)

@app.post('/delete/post')
def delete_post(post_id):
    # Need to retrieve id, and then delete it.
    post_delete = posts.query.get(post_id)
    db.session.delete(post_delete)
    db.session.commit()

    return redirect('/')
