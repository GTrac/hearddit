
from flask import Flask, redirect, render_template, request, abort, session
from flask_sqlalchemy import SQLAlchemy
from models import db, users, subh, posts, comments, comments_flag
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.reflect()
    db.drop_all()
    db.create_all()
    test_new_user1 = users(user_name='test', user_password='test_password', user_email='test@email.com')
    test_new_user2 = users(user_name='test2', user_password='test_password', user_email='test2@email.com')
    test_user_gilbert = users(user_name='gilbert', user_password='gilbert_password', user_email='gtraczyk@uncc.edu')
    db.session.add(test_new_user1)
    db.session.add(test_new_user2)
    db.session.add(test_user_gilbert)

    test_new_sub1 = subh(sub_name='test1', sub_owner=1, sub_total_users=1)
    test_new_sub2 = subh(sub_name='test2', sub_owner=2, sub_total_users=1)
    test_new_sub3 = subh(sub_name='gilberts_sub', sub_owner=3, sub_total_users=3)
    db.session.add(test_new_sub1)
    db.session.add(test_new_sub2)
    db.session.add(test_new_sub3)

    test_new_post1 = posts(post_title='test post', post_rating=1)
    test_new_post2 = posts(post_title='test post', post_link='https://www.google.com/', post_rating=1)
    test_new_post3 = posts(post_title='test post', post_text='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sapien nec sagittis aliquam malesuada bibendum arcu vitae elementum. Quis hendrerit dolor magna eget est. Eu lobortis elementum nibh tellus. Maecenas sed enim ut sem viverra aliquet eget sit. In hac habitasse platea dictumst. Non quam lacus suspendisse faucibus interdum posuere lorem ipsum. Sapien et ligula ullamcorper malesuada proin libero nunc. Malesuada bibendum arcu vitae elementum. Quam pellentesque nec nam aliquam. Nunc scelerisque viverra mauris in aliquam sem fringilla. Vel elit scelerisque mauris pellentesque pulvinar pellentesque. Pretium quam vulputate dignissim suspendisse in est ante in. Fermentum posuere urna nec tincidunt praesent semper feugiat. At quis risus sed vulputate odio. Vitae semper quis lectus nulla at volutpat diam ut. Elementum facilisis leo vel fringilla est ullamcorper eget nulla facilisi. Hendrerit gravida rutrum quisque non tellus orci ac auctor augue.', post_rating=1)
    db.session.add(test_new_post1)
    db.session.add(test_new_post2)
    db.session.add(test_new_post3)

    test_comment1 = comments(user_id=1, post_id=1, reply_id=0, comment_text='test', comment_rating=1)
    test_comment2 = comments(user_id=2, post_id=1, reply_id=1, comment_text='test comment 2', comment_rating=1)
    db.session.add(test_comment1)
    db.session.add(test_comment2)

    db.session.commit()






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


@app.get('/')
def flag_comments(comment):
    flagged_comment = comments_flag.query.get(comment)
    # Temporary
    return render_template('pin_discussions.html', flagged_comment=flagged_comment)