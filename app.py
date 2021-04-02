from flask import Flask
from flask import render_template
from flask import request 
from flask_sqlalchemy import SQLAlchemy

app = Flask("myapp12")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb/data.sqlite'

db = SQLAlchemy(app)
print(db)


@app.route("/form")
def myform():
	f = render_template("form.html")
	return f


	
@app.route("/tech", methods=["GET"])
def mymenu():

	Choice = request.args.get("x")
	#print(Choice)
	#return Choice
	if "Easy" == Choice:
		f = render_template("easy.html")
		return f

	elif "Medium" == Choice:
		f = render_template("medium.html")
		return f

	elif "Hard" == Choice:
		f = render_template("hard.html")
		return f	



class IIEC(db.Model):

	id = db.Column(db.Integer, primary_key = True)
	a1 = db.Column(db.Text, unique=True, nullable=False)
	a2 = db.Column(db.Integer, unique=True, nullable=False)
	a3 = db.Column(db.Integer, unique=True, nullable=False)
	a4 = db.Column(db.Integer, unique=True, nullable=False)
	a5 = db.Column(db.Integer, unique=True, nullable=False)

	def __init__(self, a1, a2, a3, a4, a5):
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.a4 = a4
		self.a5 = a5
		

db.create_all()


@app.route("/database1", methods=["GET"])
def database1():

	a1 = request.args.get("q1")
	a2 = request.args.get("q2")
	a3 = request.args.get("q3")
	a4 = request.args.get("q4")
	a5 = request.args.get("q5") 

	return a1+a2+a3+a4+a5

	jack = IIEC(a1, a2, a3, a4, a5)
	db.session.add(jack)
	db.session.commit()









