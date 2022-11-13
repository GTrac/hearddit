from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    #Edit once Database models are implemented
    all_posts = ''
    communities = ['h/TestCommunity1', 'h/TestCommunity2', 'h/TestCommunity3']
    return render_template('home_page.html', list_posts = True, posts = all_posts, communities = communities)


