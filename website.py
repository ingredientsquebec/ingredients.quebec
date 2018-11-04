import smtplib
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField
from wtforms.validators import DataRequired, Length, URL
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(port=27017)
db = client.iq

# Flask Settings
application = Flask(__name__)
Bootstrap(application)
application.config['SECRET_KEY'] = 'brassins_d_ici'

# Formulaires
class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    URL = StringField('URL', validators=[DataRequired()])
    code_postal = StringField('code_postal', validators=[DataRequired()])
    logo = FileField('logo')

def mail_form(submit_values, logo):
    if logo:
        msg = MIMEMultipart('related')
        msg['Subject'] = 'Nouveau détaillant'
        msg['From'] = "infos@ingredients.quebec"
        msg['To'] = "infos@ingredients.quebec"
        content = MIMEText("Nom: " + submit_values['name'] + "\n\r" + "Description: " + submit_values['description']
                           + "URL: " + submit_values['URL'] + "\n\r" + "Code Postal: " + submit_values['code_postal'])
        f = logo.stream.read()
        f = MIMEImage(f)
        msg.attach(content)
        msg.attach(f)
    else:
        msg = MIMEText("Nom: " + submit_values['name'] + "\n\r" + "Description: " + submit_values['description']
                        + "URL: " + submit_values['URL'] + "\n\r" + "Code Postal: " + submit_values['code_postal'])
        msg['Subject'] = 'Nouveau détaillant'
        msg['From'] = "infos@ingredients.quebec"
        msg['To'] = "infos@ingredients.quebec"

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('127.0.0.1')
    s.send_message(msg)
    s.quit()


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/apropos')
def apropos():
    return render_template('apropos.html')


@application.route('/malteries')
def malteries():
    result_malteries = db.malteries.find()
    return render_template('malteries.html', malteries=result_malteries)


@application.route('/houblonnieres')
def houblonnieres():
    result_houblonnieres = db.houblonnieres.find()
    return render_template('houblonnieres.html', houblonnieres=result_houblonnieres)


@application.route('/levuriers')
def levuriers():
    result_levuriers = db.levuriers.find()
    return render_template('levuriers.html', levuriers=result_levuriers)


@application.route('/ajout_detaillant', methods=['GET', 'POST'])
def ajout_detaillant():
    form = MyForm()
    if form.validate_on_submit():
        mail_form(form.data, form.logo.data)
    else:
        print("ERROR: form not complete")
    return render_template('ajout_detaillant.html', form=form)


if __name__ == '__main__':
    application.run(debug=False, host='0.0.0.0')
