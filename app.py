from flask import Flask, render_template,request,flash,redirect,url_for,session
import pandas as pd, numpy as np
import pickle
import sqlite3
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
.0

app.config["SESSION_PARMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

con=sqlite3.connect("database.db")
con.execute("create table if not exists users(id integer primary key,name text,gender text,age integer, weight integer, height integer, calorie integer,protein integer, carb integer, fat integer, gmail text,username text,password text)")
con.close()

filename = 'model.pkl'
clf = pickle.load(open(filename, 'rb'))




@app.route('/')
def index():
    if not session.get("username"):
        return redirect("/home")
    return redirect("/dashboard")
 

@app.route('/home')
def home():
    return render_template("front.html")

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        con=sqlite3.connect("database.db")
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from users where username=? and password=?",(username,password))
        data=cur.fetchone()
        
        if data:
            session["username"]=data["username"]
            session["password"]=data["password"]
            return redirect("/dashboard")
        else:
            flash("Username and Password Mismatch","red")
            return redirect(url_for("login"))
    return render_template("login.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        try:
            name=request.form['name']
            mail=request.form['mail']
            username=request.form['username']
            password=request.form['password']
            con=sqlite3.connect("database.db")
            cur=con.cursor()
            cur.execute("insert into users(name,gmail,username,password)values(?,?,?,?)",(name,mail,username,password))
            con.commit()
            con.close()
            flash("Account Created Successfully","green")
        except:
            flash("Something Went Wrong","red")
        finally:
            return redirect(url_for("login"))

    return render_template('register.html')

@app.route('/dashboard',methods=["GET","POST"])
def dashboard():
    if not session.get("username"):
        return redirect("/login")
    return render_template("dashboard.html")


@app.route('/contact',methods=["GET","POST"])
def contact():

    if not session.get("username"):
        return redirect("/login")
    return render_template("contact.html")

@app.route('/about',methods=["GET","POST"])
def about():
        if not session.get("username"):
           return redirect("/login")
        return render_template("about.html")

@app.route('/main')
def main():   
        if not session.get("username"):
           return redirect("/login")
        return render_template("home.html")


@app.route('/predict', methods = ['POST'])
def predict():
	if request.method == 'POST':
		me = request.form['message']
		message = [float(x) for x in me.split()]
		vect = np.array(message).reshape(1, -1)
		my_prediction = clf.predict(vect)
		return render_template('result.html',prediction = my_prediction)


@app.route('/logout')
def logout():
    session["username"] = None
    return redirect("/")


if __name__ == '__main__':
	app.run(debug=5000)

	
