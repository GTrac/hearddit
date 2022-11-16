from flask import Flask, redirect, render_template, request, abort, session


app = Flask(__name__)

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

@app.post('/login/create')
def create_account():
   
    email = request.form.get('email_input')
    email_confirm = request.form.get('email_confirm')
    username = request.form.get('enter_username')
    pasword = request.form.get('enter_password')

    # Need an if statement to make sure both email variables are equal. If not, then it should not go to the database.
    if email != email_confirm:
        error_message = 'Emails did not match'
        return render_template('create_account.html', error_message = error_message)

    # return render_template('create_account.html', email=email, email_confirm=email_confirm,username=username,password=password)
    return redirect('/home')

# Needed two separate functions for a post and get route.
@app.get('/login/create')
def get_create_form():
    return render_template('create_account.html')

@app.get('/create/post')
def index_four():
    return render_template('create_new_post.html')


