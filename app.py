#  global request object to access incoming request data will be submitted via HTML form.
# url_for() function to generate URLs
# redirect() function to redirect the client to a different location
from flask import Flask, render_template, url_for, redirect
# from forms.py
from forms import SurveyForm
# from config.py
from config import Config

app = Flask(__name__)
# Get credentials from config.py
app.config.from_object(Config)

# Define dictionaries. In real life this would come from a database.
responses_list = [{
    'name': 'Jane Doe',
    'organization': 'The Gunter Group',
    'email': 'janed@guntergroup.com',
    'contact': True,
    'level_q1': '1-rarely',
    'level_q2': '4-always',
    'level_q3': '1-rarely'
    }
    ,
    {
    'name': 'Enej Ode',
    'organization': 'The Thunder Group',
    'email': 'enej.ode@thundergroup.com',
    'contact': False,
    'level_q1': '4-always',
    'level_q2': '4-always',
    'level_q3': '2-sometimes'
    }
    ]


@app.route('/', methods=('GET', 'POST'))
def index():
    # save the instance of the web form
    form = SurveyForm()
    # when user submits valid form, append the contents and take them to survey page
    if form.validate_on_submit():
        responses_list.append({'name': form.name.data,
                             'organization': form.organization.data,
                             'email': form.email.data,
                             'contact': form.contact.data,
                             'level_q1': form.level_q1.data,
                             'level_q2': form.level_q2.data,
                             'level_q3': form.level_q2.data
                             })
        return redirect(url_for('responses'))
    # render the form on the index page
    return render_template('index.html', form=form)

# display the responses list
@app.route('/responses/')
def responses():
    return render_template('responses.html', responses_list=responses_list)