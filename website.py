import pymodm
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import models


def connect_to_mongodb():
    """
    Connects to the database using pymodm
    """
    # TODO The connection string must be imported from somewhere
    # TODO We can use an ini file or environment variables.
    connection_uri = "mongodb://localhost:27017/iq"
    pymodm.connect(connection_uri, alias="default")


# Flask Settings
application = Flask(__name__)
Bootstrap(application)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/apropos')
def apropos():
    return render_template('apropos.html')


@application.route('/malteries')
def malteries():
    result_malteries = models.Malterie.objects.all()
    return render_template('malteries.html', malteries=result_malteries)


@application.route('/houblonnieres')
def houblonnieres():
    result_houblonnieres = models.Houblonniere.objects.all()
    return render_template('houblonnieres.html', houblonnieres=result_houblonnieres)


@application.route('/levuriers')
def levuriers():
    result_levuriers = models.Levurier.objects.all()
    return render_template('levuriers.html', levuriers=result_levuriers)


if __name__ == '__main__':
    connect_to_mongodb()
    application.run(debug=False, host='0.0.0.0')
