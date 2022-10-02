#Created by Nayza-bytes
#Pushed on github: 02/10/2022

from flask import Flask, render_template, request
#import flask


#Create the flask app
app = Flask(__name__)

#the app.rout decorator is checking the methods that we are using
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST': #If its the 'POST' method that mean something as been pasted in the url feed
        url_received = request.form('nameh') #get whatever info give on the URL input form and store this into a variable
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