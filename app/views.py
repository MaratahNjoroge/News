from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its input
    '''
    return render_template('index.html')

# @app.route('./blog/<blog_id>')
# def movie (blog_id):

#     '''
#     View blog page function that returns the blog details page and its data
#     '''
#     return render_template('blog.html',id = blog_id)

@app.route('/blog/<int:blog_id')
def blog(blog_id):
    '''
    View blog page function  that returns the blog details and data
    '''
    return render_template('blog.html', id = blog_id)