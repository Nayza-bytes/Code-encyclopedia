#Created by Nayza-bytes
#Pushed on github: 02/10/2022

from flask import Flask

#Create the flask app
app = Flask(__name__)

#Test if our flask app is working with this function
@app.route('/')
def hello():
    return "Hello world!"

#The '@app.route' will be useful so when we are typing the url we can enter nayza at the end
#And have a different message
@app.route('/nayza')
def hi():
    return "Hi welcom coder"

#Run the flask app on port 500 with debug
if __name__ == '__main__':
    app.run(port = 500, debug = True)