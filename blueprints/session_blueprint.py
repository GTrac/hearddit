from flask import Flask, redirect, render_template, request, abort, session, Blueprint, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from src.models import db, users, community, posts, comments
from secuirty import bcrypt
import os
import base64
import spotipy
from spotipy.oauth2 import SpotifyOAuth

router = Blueprint('session', __name__)

#log in user
@router.post('/login')
def post_user_login():
    session.clear()
    username = request.form.get('email')
    password = request.form.get('password')

    existing_user = users.query.filter_by(user_name = username).first()
    existing_email = users.query.filter_by(user_email = username).first()

    if not (existing_user or existing_email):
        flash('User does not exist, try again')
        return redirect('/login')
    
    if not bcrypt.check_password_hash(existing_user.user_password, password):
        flash('User does not exist or incorrect password, try again')
        return redirect('/login')

    session['user'] = {
        'user_id':existing_user.user_id,
        'user_name': existing_user.user_name
    }

    return redirect('/')


@router.get('/login')
def get_user_login():
    return render_template('login.html')


@router.post('/signup')
def post_create_account():
    session.clear()
    email = request.form.get('email_input')
    email_confirm = request.form.get('email_confirm')
    username = request.form.get('enter_username')
    password = request.form.get('enter_password')

    if email != email_confirm:
        flash('Email dosent match, try again')
        return redirect('/signup')
    
    existing_user = users.query.filter_by(user_name = username).first()
    existing_email = users.query.filter_by(user_email = email).first()

    if (existing_user or existing_email):
        flash('user already exists, try again')
        return redirect('/signup')

    #great user dosent exist salt and pepper password
    hashed_bytes = bcrypt.generate_password_hash(password, int(os.getenv('BCRYPT_ROUNDS')))
    hashed_password = hashed_bytes.decode('utf-8')
    #save user
    new_user = users(user_name=username, user_email= email, user_password=hashed_password)   
    db.session.add(new_user)
    db.session.commit()

    session['user'] = {
        'user_id':new_user.user_id,
        'user_name': new_user.user_name
    }
    # return render_template('create_account.html', email=email, email_confirm=email_confirm,username=username,password=password)
    return redirect('/')

#get method for signup
@router.get('/signup')
def get_create_account():
    return render_template('signup.html')

#Logs user out and removes it from session
@router.post('/logout')
def logout():
    session.pop('user')
    session.clear()
    return redirect('/')




# SPOTIFY INTEGRATION FOR USER AUTH/Login/SignUp
"""
NOTES: need to change redirect uri, from local host if we deploy
ask me for token keys will not commit them to github

also if you make changes please for the love of god read the documentation for spotipy
found here: https://spotipy.readthedocs.io/en/2.21.0/?highlight=scope#module-spotipy.oauth2
"""
@router.get('/signup/spotifty')
def signup_spotify():
    spotify_auth = create_spotify_oauth()
    auth_url = spotify_auth.get_authorize_url()
    return redirect(auth_url)
    
@router.get('/login/spotifty')
def login_spotify():
    spotify_auth = create_spotify_oauth()
    auth_url = spotify_auth.get_authorize_url()
    return redirect(auth_url)

@router.get('/authorize')
def authorize():
    #need to create a user token for spotify to work
    spotify_auth = create_spotify_oauth()
    session.clear()
    c = request.args.get('code')
    token = spotify_auth.get_access_token(c)
    session['token'] = token
    sp = spotipy.Spotify(auth=session.get('token').get('access_token'))
    currrent_user = sp.current_user()
    username = currrent_user['display_name']
    user_email = currrent_user['email']
    
    existing_user = users.query.filter_by(user_email = user_email).first()
    if not existing_user:
        #need to create a placeholder for spotify users in db
        #need a unique username -> could just repeat passwords hashing
        #great user dosent exist salt and pepper password
        hashed_bytes = bcrypt.generate_password_hash(username, int(os.getenv('BCRYPT_ROUNDS')))
        new_username = hashed_bytes.decode('utf-8')

        #hash password
        hashed_bytes = bcrypt.generate_password_hash(user_email, int(os.getenv('BCRYPT_ROUNDS')))
        hashed_password = hashed_bytes.decode('utf-8')
        #save user
        new_user = users(user_name=new_username, user_email= user_email, user_password=hashed_password)   
        db.session.add(new_user)
        db.session.commit()

        session['user'] = {
            'user_id': new_user.user_id,
            'user_name': username
        }
        return redirect('/')
    
    session['user'] = {
        'user_id':existing_user.user_id,
        'user_name': username
    }
    return redirect('/')


#funtion to create oauth
def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'), 
        client_secret=os.getenv('SPOTIFY_SECRET'), 
        redirect_uri=url_for('session.authorize', _external = True),
        scope='user-read-email, user-library-read')