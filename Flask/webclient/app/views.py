import requests
from flask import request, redirect, render_template, url_for, json
from app import app

@app.route('/')

@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':
		_username = request.form['username']
		_password = request.form['password']

		url = 'http://127.0.0.1/api/user'
		q = {'filters': [{'name': 'username', 'op': 'eq', 'val': _username}, {'name': 'password', 'op': 'eq', 'val': _password}]}
		response = requests.get(url, params={'q': json.dumps(q)})
		r = response.json()
		if r['num_results'] == 0:
			return render_template('login.html')
		else:
			return redirect("/manager", code=302)
	else:
		return render_template('login.html')

@app.route('/manager')
def manager():
	active1="class=active"
	active2="class=active"
	active3="class=active"
	
	if request.args.get('id') == None:
		id = 1
	else:
		id = request.args.get('id')
		id = int(id)
	
		if id == 1:
			url = 'http://127.0.0.1/api/task'
			result = requests.get(url)
			response = json.loads(result.text)		
			return render_template('pendingtask.html', active1=active1, response=response)
		elif id == 2:
			return render_template('completetask.html', active2=active2)
		elif id == 3:
			return render_template('profile.html', active3=active3)
		else:
			return render_template('pendingtask.html', active1=active1)
