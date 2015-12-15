import requests
import time
from flask import request, redirect, render_template, url_for, json
from app import app

@app.route('/')
@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':
		_username = request.form['username']
		_password = request.form['password']
		_session = None
		_name = None
		url = 'http://127.0.0.1/api/user'
		q = {'filters': [{'name': 'username', 'op': 'eq', 'val': _username}, {'name': 'password', 'op': 'eq', 'val': _password}]}
		response = requests.get(url, params={'q': json.dumps(q)})
		r = response.json()
		_session = r['objects'][0]['id']
		if r['num_results'] == 0:
			return render_template('login.html')
		else:
			return redirect("/manager/" + str(_session) , code=302)
	else:
		return render_template('login.html')

@app.route('/manager/<int:params>/newtask', methods=['POST'])
def newtask(params):

	active1="class=active"
	url = "http://localhost/api/task"
	headers = {"Content-Type": "application/json"}
	_user_id = request.form['user_id']
	_title = request.form['title']
	_category = request.form['category']
	_priority = request.form['priority']
	_status = request.form['status']
	_expiry_date = request.form['expiry_date']
	_description = request.form['description']

	data = dict({"title": str(_title), "user_id": int(_user_id), "priority_id": int(_priority), "category_id": int(_category), "status_id": int(_status), "expiry_date": str(_expiry_date), "creation_date": str(time.strftime("%Y/%m/%d")), "description": str(_description), "last_connection": str(time.strftime("%Y/%m/%d")) })
	response = requests.post(url, data=json.dumps(data), headers=headers) 
	print response.status_code
	#assert response.status_code == 200

	return redirect("/manager/" + str(_user_id))

@app.route("/manager/<int:params>")
def manager(params):
	active1="class=active"
	active2="class=active"
	active3="class=active"

	if request.args.get('id') == None:
		id = 1
	else:
		id = int(request.args.get('id'))
	
	if id == 1:
		url = 'http://127.0.0.1/api/task'
		result = requests.get(url)
		response = json.loads(result.text)		
		return render_template('pendingtask.html', active1=active1, response=response, user_id=params, list_cat=get_category(), list_status = get_status(), list_prio = get_priority())
	elif id == 2:
		return render_template('completetask.html', active2=active2)
	elif id == 3:
		return render_template('profile.html', active3=active3)
	elif id == 4:
		return render_template('newtask.html', list_cat=get_category(), list_status = get_status(), list_prio = get_priority(), user_id=params)
	else:
		return render_template('pendingtask.html', active1=active1)

def get_category():
	url = 'http://127.0.0.1/api/category'
	result = requests.get(url)
	response_category = json.loads(result.text)	
	return response_category

def get_status():
	url = 'http://127.0.0.1/api/status'
	result = requests.get(url)
	response_status = json.loads(result.text)	
	return response_status

def get_priority():
	url = 'http://127.0.0.1/api/priority'
	result = requests.get(url)
	response_priority = json.loads(result.text)	
	return response_priority