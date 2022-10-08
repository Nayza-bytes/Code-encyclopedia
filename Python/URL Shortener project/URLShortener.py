#Created by Nayza-bytes

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import flask_sqlalchemy

#import flask


#Create the flask app and config the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db' #Hold the location of the SQL database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #remove trackings modification

db = SQLAlchemy(app) #store the SQLAlchemy db in a variable


#This is called a Database model \/
class Urls(db.Model):  
    id_ = db.Column('id_', db.Integer, primary_key=True) #this will created a column with Ids taht storing integer (db.Integer function), Primary key= each object will have their own id
    long = db.Column('long', db.String()) #Create a column for the long URL
    short = db.Column('short', db.String(3)) #Create a column for the short URL
#                                        ^
#               this indicated that we will never have a url longer than 3 characters

#Constructor for making object of the class
    def __init__(self, long, short):
        self.long = long
        self.short = short 
        
#Create all of the columns in the database before any requests
@app.before_first_request
def create_tables():
    db.create_all

def shorten_url():
    return 'fjk'

#the app.rout decorator is checking the methods that we are using
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST': #If its the 'POST' method that mean something as been pasted in the url feed
        url_received = request.form('nameh') #get whatever info give on the URL input form and store this into a variable
        found_url = Urls.query.filter_by(long=url_received).first()

        if found_url:
            return redirect(url_for('display_short_url', url=found_url.short))
        else:
            short_url = shorten_url()
            new_url = Urls(url_received, short_url)
            db.sessions.add(new_url)
            db.session.commit()
            return short_url
        return url_received
    else:
        return render_template('base.html')

#The '@app.route' will be useful so when we are typing the url we can enter nayza at the end
#And have a different message
#@app.route('/nayza')
#def hi():
#    return "Hi welcome coder"

#Run the flask app on port 5000 with debug
if __name__ == '__main__':
    app.run(port = 5000, debug = True)