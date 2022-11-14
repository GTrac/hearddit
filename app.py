from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('home_page.html')
    
@app.get('/post')
def index():
    return render_template('savingposts.html')

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

