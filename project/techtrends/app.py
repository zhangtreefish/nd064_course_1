# pylint: disable=missing-module-docstring
# pylint: disable=E1101
# pylint: disable=W0603
import sqlite3
import sys
from logging.config import dictConfig
from flask import Flask, json, render_template, request, url_for, redirect, flash

# configure logging to override the default beginning level of warning in Python
# https://flask.palletsprojects.com/en/2.0.x/logging/
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
    },
    'DB_CONNECTION_COUNT': 0
})

# initialise counts:
DB_CONNECTION_COUNT = 0


def get_db_connection():
    """
    Function to get a database connection. This function
    connects to database with the name `database.db`
    """
    global DB_CONNECTION_COUNT
    connection = sqlite3.connect('database.db')
    DB_CONNECTION_COUNT += 1
    connection.row_factory = sqlite3.Row
    return connection


def get_post(post_id):
    """Function to get a post using its ID"""
    connection = get_db_connection()
    the_post = connection.execute('SELECT * FROM posts WHERE id = ?',
                                  (post_id,)).fetchone()
    connection.close()
    return the_post


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
    """
    Define how each individual article is rendered;
    If the post ID is not found a 404 page is shown
    """
    the_post = get_post(post_id)
    if the_post is None:
        app.logger.error("no article by the id available")
        sys.stderr.write("no article by the id available")
        return render_template('404.html'), 404

    app.logger.info("article retrieved; title: " + the_post.title)
    sys.stdout.write("article retrieved; title: " + the_post.title)
    return render_template('post.html', post=the_post)


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
            app.logger.info(
                f"article added; id: {cursor.lastrowid} , title: {title}")
            sys.stdout.write(
                f"article added; id: {cursor.lastrowid} , title: {title}")
            cursor.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route("/healthz")
def check_health():
    """Provide Healthcheck endpoint as best practice"""
    app.logger.info('Inside /healthz endpoint')
    response = app.response_class(
        response=json.dumps({"result": " OK - healthy"}),
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
    global DB_CONNECTION_COUNT
    response = app.response_class(
        response=json.dumps(
            {"DB_CONNECTION_COUNT": DB_CONNECTION_COUNT, "post_count": len(posts)}),
        status=200,
        mimetype='application/json'
    )
    return response


# start the application on port 3111
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3111')
