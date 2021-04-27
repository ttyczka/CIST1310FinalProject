from	flask	import	Flask
from    flask   import  render_template
from    flask   import  url_for
from    flask   import  request
from    flask_bootstrap import  Bootstrap 
app	=	Flask(__name__)

import sqlite3 as sql
Bootstrap(app)

@app.route('/')
def	hello_world():
    return	'Hello	World!!'

@app.route("/welcome")
def	welcome_page():
    return	"Hello and welcome to my site!""    ¡Hola y bienvenidos a mi sitio!"

@app.route("/greetings/<season>")
def	greetings_page(season):
    if season == "christmas":
        return	"Merry Christmas"
    if season == "newyear":
        return "Happy New Year"

#def create_database():
#    conn = sql.connect("database.db")
#    conn.execute("CREATE TABLE users (name TEXT, phone TEXT, email TEXT, registration TEXT, username TEXT)")
#    conn.close()

#create_database()


@app.route("/save/<string:name>/<string:phone>/<string:email>/<string:registration>/<string:username>")
def save_data(name, phone, email, registration, username):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO users (name, phone, email, registration, username) VALUES (?, ?, ?, ?, ?)", [name, phone, email, registration, username] )
    con.commit()

    return "Record successfully added {0} {1} {2} {3} {4}". format(name, phone, email, registration, username)



@app.route("/userinfo")
def userinfo_data():
    con = sql.connect("database.db")
    con.row_factory = sql.Row 

    cur = con.cursor()
    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()
    return render_template("userinfo.html", rows = rows)

@app.route("/myform")
def new_user():
    return render_template("myform.html")

@app.route("/addrec", methods=["POST"])
def addrec():
    if request.method == "POST":
        name = request.form ["nm"]
        phone = request.form ["pho"]
        email = request.form ["eml"]
        registration = request.form ["reg"]
        username = request.form ["usn"]

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users (name, phone, email, registration, username) VALUES (?, ?, ?, ?, ?)", [name, phone, email, registration,username] )
        con.commit()
    return render_template("userinfo.html")

if	__name__	== "__main__":
    app.run(debug=True)
