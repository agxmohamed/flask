from flask import request, redirect, render_template, url_for
from app import app

@app.route('/')
@app.route('/login')
def index():
	return render_template('login.html')
@app.route('/manager')
def manager():
	id = request.args.get('id')
	id = int(id)
	active1="class=active"
	active2="class=active"
	active3="class=active"

	if id == 1:
		return render_template('pendingtask.html', active1=active1)
	elif id == 2:
		return render_template('completetask.html', active2=active2)
	elif id == 3:
		return render_template('profile.html', active3=active3)
	else:
		return render_template('pendingtask.html', active1=active1)