from flask import Flask, redirect, render_template, request, abort, session, Blueprint, flash
from flask_sqlalchemy import SQLAlchemy
from src.models import db, users, community, posts, comments
from secuirty import bcrypt
import os

router = Blueprint('session', __name__)

#log in user
@router.post('/login')
def post_user_login():
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
   
    email = request.form.get('email_input')
    email_confirm = request.form.get('email_confirm')
    username = request.form.get('enter_username')
    password = request.form.get('enter_password')

    if email != email_confirm:
        flash('Email dosent match, try again')
        return redirect('/signup')
    
    existing_user = users.query.filter_by(user_name = username).first()
    existing_email = users.query.filter_by(user_email = username).first()

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
    return redirect('/')