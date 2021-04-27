from	flask	import	Flask
from    flask   import  render_template
from    flask   import  url_for
from    flask   import  request 
from    flask_bootstrap import  Bootstrap 

import  sqlite3 as sql
app	=	Flask(__name__)
Bootstrap(app)

@app.route('/')
def	hello_world():
    return	"Hello	World"

@app.route("/index/")
def	index_page():
    return	render_template("index.html")

@app.route("/boot")
def boot_page():
    return render_template("boot.html")


@app.route('/page/<string:message>')
def	page_message(message):
    return "You entered {0}" .format(message)

@app.route('/number/num')
def	number_num(num):
    return "You entered {0}" .format(num)

@app.route('/user/username')
def	user_page(num):
    if username=='admin':
        return "Welcome Admin"
    else:
        return "Welcome User" 

@app.route("/save/<string:name>/<string:addr>/<string:city>")
def save_data(name, addr, city):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO students (name, address, city) VALUES (?, ?, ?)", [name, addr, city] )
    con.commit()

    return "Record successfully added {0} {1} {2}". format(name, addr, city)

@app.route("/list")
def list_data():
    con = sql.connect("database.db")
    con.row_factory = sql.Row 

    cur = con.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()
    return render_template("list.html", rows = rows)

@app.route("/student")
def new_student():
    return render_template("student.html")

@app.route("/addrec", methods=["POST"])
def addrec():
    if request.method == "POST":
        name = request.form ["nm"]
        addr = request.form ["add"]
        city = request.form ["cty"]

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name, address, city) VALUES (?, ?, ?)", [name, addr, city] )
        con.commit()
    return render_template("list.html")

#def create_database():
 #   conn = sql.connect("database.db")
  #  conn.execute("CREATE TABLE students (name TEXT, address TEXT, city TEXT)")
   # conn.close()

#create_database()

if	__name__	== '__main__':
    app.run(debug=True)
