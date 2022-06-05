#  global request object to access incoming request data will be submitted via HTML form.
# url_for() function to generate URLs
# flash() function to flash message when request is processed (requires setting a secret key)
# redirect() function to redirect the client to a different location
from flask import Flask, render_template, request, url_for, flash, redirect
from config import Config

app = Flask(__name__)
# Get credentials from config.py
app.config.from_object(Config)

# Define some messages to display. This could be KV pairs data in real life.
messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/create/', methods=('GET','POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # flash a mesage if fields are incomplete
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        # if fields are complete, add the form contents to the index page. Then redirect to index.
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))
    return render_template('create.html')