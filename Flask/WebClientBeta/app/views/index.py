import views

@app.route('/')
@app.route('/login', methods=['POST'])
def login():
	return render_template('index.html')

@app.route('/taskmanager')
def manager():
	return render_template('task.html')