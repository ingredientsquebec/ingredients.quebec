from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from pymongo import MongoClient



# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(port=27017)
db = client.iq

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


if __name__ == '__main__':
    application.run(debug=False, host='0.0.0.0')


