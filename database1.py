from flask import Flask
from flask import render_template
from flask import request
import subprocess as sp

def database1():

	a1 = request.args.get("q1a")
	a2 = request.args.get("q1b")
	a3 = request.args.get("q1c")
	a4 = request.args.get("q1d")

	return a1, a2, a3, a4

