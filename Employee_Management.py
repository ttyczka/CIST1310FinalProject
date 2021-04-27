from	flask	import	Flask
app	=	Flask(__name__)

@app.route('/')
def	hello_world():
    return	'Welcome!'

@app.route('/Login')
def	hello_world():
    return	'Welcome Employees and New Users!'

if	__name__	== "__main__":
    app.run()
