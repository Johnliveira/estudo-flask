from flask import render_template
from app import app


@app.route("/index/")
@app.route("/")
def index():
	return render_template('/index.html')


@app.route("/login")
def login():
	return render_template('/base.html')


#@app.route("/test", defaults={'name': None})
#@app.route("/test/<name>")
#def test(name):
#	if name:
#		return "Olá, %s!" % name
#	else:
#		return "Olá, usuário!"