from	flask	import	Flask
from    flask   import  render_template
from    flask   import  url_for
from    flask   import  request 
from    flask_bootstrap import  Bootstrap 

import  sqlite3 as sql
app	=	Flask(__name__)
Bootstrap(app)
##def create_database():
  ##conn = sql.connect("Employeedatabase.db")
  ##conn.execute("CREATE TABLE Users (EmployeeID INTEGER, UserName TEXT, FirstName TEXT, LastName TEXT, Email TEXT, Phone TEXT, Password TEXT)")
  ##conn.execute("CREATE TABLE Time_Sheet (SheetID INTEGER, EmployeeID INTEGER, Monday_Hours INTEGER, Tuesday_Hours INTEGER, Wednesday_Hours INTEGER, Thursday_Hours INTEGER, Friday_Hours INTEGER, Total_Hours INTEGER)")
  ##conn.close()

##create_database()

@app.route('/')
def	hello_world():
    return	'Hello!'

@app.route("/Login")
def	Login_page():
    return	render_template("Login.html")

@app.route("/EmployerPageOptions")
def	EmployerPageOptions_page():
    return	render_template("EmployerPageOptions.html")



@app.route("/NewUserInfo")
def new_user():
    return render_template("NewUserInfo.html")
    
@app.route("/Addnewuser", methods=["POST"])
def Addnewuser():
    if request.method == "POST":
        EmployeeID = request.form ["EmployeeID"]
        UserName = request.form ["UserName"]
        FirstName = request.form ["FirstName"]
        LastName = request.form ["LastName"]
        Email = request.form ["Email"]
        Phone = request.form ["Phone"]
        Password= request.form ["Password"]
        
        with sql.connect("Employeedatabase.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Users (EmployeeID, UserName, FirstName, LastName, Email, Phone, Password) VALUES (?, ?, ?, ?, ?, ?, ?)", [EmployeeID, UserName, FirstName, LastName, Email, Phone, Password] )
            con.commit()
            con.row_factory = sql.Row 

            cur = con.cursor()
            cur.execute("SELECT * FROM Users")

            rows = cur.fetchall()
        return render_template("EmployeeContacts.html",rows = rows)

@app.route("/EmployeeContacts")
def EmployeeContacts_data():
    con = sql.connect("Employeedatabase.db")
    con.row_factory = sql.Row 

    cur = con.cursor()
    cur.execute("SELECT * FROM Users")

    rows = cur.fetchall()
    return render_template("EmployeeContacts.html", rows = rows)

@app.route("/EmployeeTimeSheets")
def EmployeeTimeSheets_data():
    con = sql.connect("Employeedatabase.db")
    con.row_factory = sql.Row 

    cur = con.cursor()
    cur.execute("SELECT * FROM Time_Sheet")

    rows = cur.fetchall()
    return render_template("EmployeeTimeSheets.html", rows = rows)

@app.route("/EmployeeLogTime")
def EmployeeLogTime():
    return render_template("EmployeeLogTime.html")

@app.route("/timelogged", methods=["POST"])
def timelogged():
    if request.method == "POST":
        SheetID = request.form ["SheetID"]
        EmployeeID = request.form ["EmployeeID"]
        Monday_Hours = request.form ["Monday_Hours"]
        Tuesday_Hours = request.form ["Tuesday_Hours"]
        Wednesday_Hours = request.form ["Wednesday_Hours"]
        Thursday_Hours = request.form ["Thursday_Hours"]
        Friday_Hours = request.form ["Friday_Hours"]
        Total_Hours = request.form ["Total_Hours"]
        
        with sql.connect("Employeedatabase.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Time_Sheet (SheetID, EmployeeID, Monday_Hours, Tuesday_Hours, Wednesday_Hours, Thursday_Hours, Friday_Hours, Total_Hours) VALUES (?, ?, ?, ?, ?, ?, ?,?)", [SheetID, EmployeeID, Monday_Hours,Tuesday_Hours, Wednesday_Hours, Thursday_Hours, Friday_Hours, Total_Hours] )
            con.commit()
    return render_template("EmployeeTimeSheets.html")

if	__name__	== "__main__":
    app.run()