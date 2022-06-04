from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template('create.html')