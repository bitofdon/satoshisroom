from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


#home page
@app.route('/')
@app.route('/index')
def index():
    #fake user for now for testing purposes
    user = {'username': 'Satoshi'}
    #fake object for testing purposes - make fake list of blog posts
    posts = [
        {
            'author': {'username':'Satoshi'},
            'body': 'This is a sample post'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


#login page
@app.route('/login', methods=['GET', 'POST'] )
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #flash a message to the user
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data ))
        return redirect(url_for('index') )
    return render_template('login.html', title='Sign In', form=form)
