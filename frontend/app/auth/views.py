from . import auth_blueprint
from flask import render_template, request, redirect, url_for


@auth_blueprint.route('/register/<string:email>')
def register(email):
    message_data={
        'subject': 'Hello from the flask app!',
        'body': 'This email was sent asynchronously using Celery.',
        'recipients': email,

    }
    return render_template('auth/index.html', email=email)