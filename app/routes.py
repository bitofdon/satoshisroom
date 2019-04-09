from flask import render_template
from app import app



#home page
@app.route('/')
@app.route('/index')
def index():
        #code here
        #...
    return render_template('index.html')

#blog page
# @app.route('/blog')
# def blog():
#     #code here..
#     return render_template('blog.html')


#login page
# @app.route('/login')
# def login():
#    #code here..
#     return render_template('login.html')
