import requests
from flask import request, redirect, render_template, url_for, json
from app import app

@app.route('/')
@app.route('/login', methods=['POST'])
def login():
	#SI RECIBO EL METODO POST
	if request.method == 'POST':
		#URL A DONDE CONSULTO LOS USUARIOS
		url = 'http://127.0.0.1/api/user'
		#Obtengo el usuario y el password del formulario de login
		_username = request.form['username']
		_password = request.form['password']
		#Creo una variable para mi "sesion"
		_session = None
		#Genero el filtro de lo que necesito buscar
		query = {'filters': [{'name': 'username', 'op': 'eq', 'val': _username}, {'name': 'password', 'op': 'eq', 'val': _password}]}
		#Obtengo el query que le doy a la api
		response = requests.get(url, params={'query': json.dumps(query)})
		#Guardo el json que me devolvio la api
		r = response.json()
		#Obtengo el id del usuario y lo guardo en mi variable de "sesion"
		_session = r['objects'][0]['id']
		#Si no me devuelve un id valido
		if r['num_results'] == 0:
			#regreso al login
			return render_template('index.html')
		#Sino,
		else:
			#Voy al administador
			return redirect("/taskmanager/" + str(_session) , code=302)
	#Sino,
	else:
		#Muestro el login
		return render_template('index.html')		

@app.route('/taskmanager/<int:params>')
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
		return render_template('activetask.html', active1=active1, response=response, user_id=params)
	elif id == 2:
		return render_template('task.html', active2=active2)
	elif id == 3:
		return render_template('task.html', active3=active3)
	elif id == 4:
		return render_template('task.html', list_cat=get_category(), list_status = get_status(), list_prio = get_priority(), user_id=params)
	else:
		return render_template('task.html', active1=active1)

	return render_template('task.html')

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
