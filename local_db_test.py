
import pymysql
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SelectField, SubmitField
from flask_bootstrap import Bootstrap5


# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy()
# create the app
app = Flask(__name__)

# make sure the database username, database password and
# database name are correct
username = 'username'
password = 'password'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
# keep this as is for a hosted website
server  = 'isabellasdouglas.com'
# CHANGE to YOUR database name, with a slash added as shown
dbname   = '/isabel32_elections'
# there is no socket

# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'coolbeans22'

# initialize the app with Flask-SQLAlchemy
db.init_app(app)

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)


# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all of your columns by name and data type as shown

# votersbycounty
class Election(db.Model):
    __tablename__ = 'votersbycounty'
    countyCode = db.Column(db.String, primary_key=True)
    totalVoters22 = db.Column(db.Integer)
    totalActiveVoters22 = db.Column(db.Integer)
    rep22 = db.Column(db.Integer)
    dem22 = db.Column(db.Integer)
    npa22 = db.Column(db.Integer)
    oth22 = db.Column(db.Integer)
    totalVoters18 = db.Column(db.Integer)
    totalActiveVoters18 = db.Column(db.Integer)
    rep18 = db.Column(db.Integer)
    dem18 = db.Column(db.Integer)
    npa18 = db.Column(db.Integer)
    oth18 = db.Column(db.Integer)

# countyAge
class Age(db.Model):
    __tablename__ = 'countyAge'
    countyCode = db.Column(db.String, primary_key=True)
    age1_22 = db.Column(db.Integer)
    age2_22 = db.Column(db.Integer)
    age3_22 = db.Column(db.Integer)
    age4_22 = db.Column(db.Integer)
    age1_18 = db.Column(db.Integer)
    age2_18 = db.Column(db.Integer)
    age3_18= db.Column(db.Integer)
    age4_18 = db.Column(db.Integer)

#countyGender
class Gender(db.Model):
    __tablename__ = 'countyGender'
    countyCode = db.Column(db.String, primary_key=True)
    female_22 = db.Column(db.Integer)
    male_22 = db.Column(db.Integer)
    unknown_22 = db.Column(db.Integer)
    female_18 = db.Column(db.Integer)
    male_18 = db.Column(db.Integer)
    unknown_18= db.Column(db.Integer)
#countyRace
class Race(db.Model):
    __tablename__ = 'countyRace'
    countyCode = db.Column(db.String, primary_key=True)
    race1_22 = db.Column(db.Integer)
    race2_22 = db.Column(db.Integer)
    race3_22 = db.Column(db.Integer)
    race4_22 = db.Column(db.Integer)
    race5_22 = db.Column(db.Integer)
    race1_18 = db.Column(db.Integer)
    race2_18 = db.Column(db.Integer)
    race3_18= db.Column(db.Integer)
    race4_18 = db.Column(db.Integer)
    race5_18 = db.Column(db.Integer)



# get ID-name pairs to use in a select menu
# the query below does not work without app_context()
# see https://flask.palletsprojects.com/en/2.2.x/appcontext/
with app.app_context():
    # get IDs and names for the select menu BELOW
    votersbycounty  = db.session.execute(db.select(Election)
        .order_by(Election.countyCode)).scalars()
    # create the list of tuples needed for the choices value
    pairs_list = []
    for election in votersbycounty:
        pairs_list.append( (election.countyCode, election.countyCode ) )

# Flask-WTF form magic

class ElectionSelect(FlaskForm):
    select = SelectField( 'Choose a county:',
      choices=pairs_list
      )
    submit = SubmitField('Submit')

# routes

# starting page for app
@app.route('/')
def index():
    # make an instance of the WTF form class we created, above
    form = ElectionSelect()
    # pass it to the template
    return render_template('index.html', form=form)


# whichever id comes from the form, that one will be displayed
@app.route('/county', methods=['POST'])
def election_detail():
    election_countyCode = request.form['select']

    # get all columns for the one with the supplied id
    the_election = db.get_or_404(Election, election_countyCode)

    the_age = db.get_or_404(Age, election_countyCode)

    the_gender = db.get_or_404(Gender, election_countyCode)

    the_race = db.get_or_404(Race, election_countyCode)

    # pass it to the template
    return render_template('election.html', the_election=the_election, the_age=the_age, the_gender=the_gender, the_race=the_race)


@app.route('/election/<county_code>')
def election(county_code):
    the_election = get_election(county_code)
    return render_template('election.html', the_election=the_election, county=county_code)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=4999, debug=True)
