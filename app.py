import os
from flask import Flask,render_template,request,session,flash,url_for,redirect
from flask_mail import Mail, Message
from celery import Celery

app = Flask(__name__)

mail_sender=os.environ.get('MAIL_USERNAME')
mail_password=os.environ.get('MAIL_PASSWORD')
app.secret_key ='yH9UIOPAJUAAJAjAJAAj'

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'iamgilwell@gmail.com'
app.config['MAIL_PASSWORD'] = 'somepassword'
app.config['MAIL_DEFAULT_SENDER'] = 'iamgilwell@gmail.com'
mail = Mail(app)

celery = Celery(app.name,broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html',email=session.get('email',''))
    email = request.form['email']
    session['email'] = email

    # Send the email
    email_data = {
        'subject':'Hello Welcome to Debugging',
        'to':email,
        'body':'It is working!!'
    }

    if request.form['submit'] == 'Send':
        # Send right away
        send_async_email.delay(email_data)
        flash('Sending email to {0}'.format(email))
    else:
        # send in one minute
        send_async_email.apply_async(args=[email_data],countdown=60)
        flash('An email will be sent to {0} in one minute'.format(email))

    return redirect(url_for('index'))

@celery.task
def send_async_email(email_data):
    """ Background task to send an email with Flask-Email """

    msg = Message(email_data['subject'],sender=app.config['MAIL_DEFAULT_SENDER'],recipients=[email_data['to']])
    msg.body = email_data['body']
    with app.app_context():
        mail.send(msg)