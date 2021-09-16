import sqlite3

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
#from werkzeug.exceptions import abort
import logging
import sys
# configure logging to override the default beginning level of warning in Python
#https://flask.palletsprojects.com/en/2.0.x/logging/
from logging.config import dictConfig
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# initialise counts:
db_connection_count = 0

def get_db_connection():
    """Function to get a database connection. This function connects to database with the name `database.db`"""
    global db_connection_count
    connection = sqlite3.connect('database.db')
    db_connection_count += 1
    connection.row_factory = sqlite3.Row
    return connection

def get_post(post_id):
    """Function to get a post using its ID"""
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    return post

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    """Define the main route of the web application"""
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    """Define how each individual article is rendered; If the post ID is not found a 404 page is shown"""
    thePost = get_post(post_id)
    if thePost is None:
        app.logger.error("no article by the id available")
        sys.stderr.write("no article by the id available")
        return render_template('404.html'), 404
    else:
        app.logger.info("article retrieved; title: " + thePost.title)
        sys.stdout.write("article retrieved; title: " + thePost.title)
        return render_template('post.html', post=thePost)

@app.route('/about')
def about():
    """Define the About Us page"""
    app.logger.info("someone has reached /about")
    sys.stdout.write("someone has reached /about")
    return render_template('about.html')

@app.route('/create', methods=('GET', 'POST'))
def create():
    """Define the post creation functionality"""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            app.logger.info("article added; id: %d , title: %s" %(cursor.lastrowid, title))
            sys.stdout.write("article added; id: %d , title: %s" %(cursor.lastrowid, title))
            cursor.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route("/healthz")
def check_health():
    """Provide Healthcheck endpoint as best practice"""
    app.logger.info('Inside /healthz endpoint')
    response = app.response_class(
        response=json.dumps({"result":" OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Status request successfull')
    return response

@app.route("/metrics")
def show_metrics():
    """Provide metrics endpoint as best practice"""
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    global db_connection_count
    response = app.response_class(
        response=json.dumps({"db_connection_count": db_connection_count, "post_count": len(posts)}),
        status=200,
        mimetype='application/json'
    )
    return response

# start the application on port 3111
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3111')
