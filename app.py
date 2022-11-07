from flask import Flask, redirect, render_template, request, abort


app = Flask(__name__)

@app.get('/')
def index():
    return render_template('home_page.html')

@app.get('/login')
def index():
    return render_template('login.html')

@app.get('/home')
def index():
    return render_template('home_page.html')

@app.post('/login/create')
def create_account():
    email = request.form.get('email_input')
    email_confirm  = request.form.get('email_confirm')
    username = request.form.get('enter_username')
    password = request.form.get('enter_password')


    # Need an if statement to make sure both email variables are equal. If not, then it should not go to the database.
    if email != email_confirm:
        abort(400)
    


    # return render_template('create_account.html', email=email, email_confirm=email_confirm,username=username,password=password)
    return redirect('/home')

# Needed two separate functions for a post and get route.
@app.get('/login/create')
def get_create_form():
    return render_template('create_account.html')

@app.get('/create/post')
def index():
    return render_template('create_new_post.html')

