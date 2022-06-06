#  global request object to access incoming request data will be submitted via HTML form.
# url_for() function to generate URLs
# redirect() function to redirect the client to a different location
from flask import Flask, render_template, url_for, redirect
# from forms.py
from forms import CourseForm
# from config.py
from config import Config

app = Flask(__name__)
# Get credentials from config.py
app.config.from_object(Config)

# Define dictionaries. In real life this would come from a database.
courses_list = [{
    'title': 'Python 101',
    'description': 'Learn Python basics',
    'price': 34,
    'available': True,
    'level': 'Beginner'
    }]


@app.route('/', methods=('GET', 'POST'))
def index():
    # save the instance of the web form
    form = CourseForm()
    # when user submits valid form, append the contents and take them to courses page
    if form.validate_on_submit():
        courses_list.append({'title': form.title.data,
                             'description': form.description.data,
                             'price': form.price.data,
                             'available': form.available.data,
                             'level': form.level.data
                             })
        return redirect(url_for('courses'))
    # render the form on the index page
    return render_template('index.html', form=form)

# display the course list
@app.route('/courses/')
def courses():
    return render_template('courses.html', courses_list=courses_list)