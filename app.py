from flask import Flask, render_template, url_for, request
import pandas as pd, numpy as np
import pickle

app = Flask(__name__)

filename = 'model.pkl'
clf = pickle.load(open(filename, 'rb'))

@app.route('/')
def index():
    return render_template("front.html")

@app.route('/login',methods=["GET","POST"])
def login():
    return render_template("login.html")

@app.route('/welcome ',methods=["GET","POST"])
def welcome():
    
      return render_template("welcome.html")

@app.route('/contact',methods=["GET","POST"])
def contact():
    return render_template("contact.html")

@app.route('/about',methods=["GET","POST"])
def about():
    return render_template("about.html")

@app.route('/main//welcome/Sam//88//-9794741477///welcome//_CW55HF8NVT*MTY4NjY3NDU0Mi4xLjEuMTY4NjY3NDU2MC4wLjAuMA//////welcome//Samprit//Mainpage mainframe')
def home():   
       return render_template("home.html")


@app.route('/predict', methods = ['POST'])
def predict():
	if request.method == 'POST':
		me = request.form['message']
		message = [float(x) for x in me.split()]
		vect = np.array(message).reshape(1, -1)
		my_prediction = clf.predict(vect)
		return render_template('result.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=5000)

	
