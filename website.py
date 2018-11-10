from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from mail_form_detaillant import mail_form_detaillant
from iqforms import DetaillantForm


# connect to MongoDB
client = MongoClient(port=27017)
db = client.iq

# Flask Settings
application = Flask(__name__)
Bootstrap(application)
application.config['SECRET_KEY'] = 'change_me_in_prod'


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


@application.route('/detaillants')
def detaillants():
    result_detaillants = db.detaillants.find()
    return render_template('detaillants.html', detaillants=result_detaillants)


@application.route('/ajout_detaillant', methods=['GET', 'POST'])
def ajout_detaillant():
    form = DetaillantForm()
    if form.validate_on_submit():
        mail_form_detaillant(form.data, form.logo.data)
        return render_template('ajout_detaillant_succes.html')
    else:
        print("ERROR: form not complete")
    return render_template('ajout_detaillant.html', form=form)


if __name__ == '__main__':
    application.run(debug=False, host='0.0.0.0')
