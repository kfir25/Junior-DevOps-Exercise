from flask import Flask, render_template, request
import mysql.connector, yaml
from flask_mysqldb import MySQL


app = Flask(__name__)

# initialize connection to database 'namelist' in mysql server < first try to connect the DB
# def init_db():
#     return mysql.connector.connect(
#         password='root', 
#         user='root', 
#         host='bdb', 
#         database='namelist'
#                                 )


#Configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)


# default page of the application
@app.route('/')
def index():
    return render_template('base.html')


#make the page visible > click "Hello" button
@app.route('/hello', methods=['GET'])
def say_hello_get():
    return render_template('hello.html')


#create a new username and insert it to the 'Username' table in the database
@app.route('/hello', methods = ['POST'])
def say_hello():
    Uname = request.form['name']
    try:
       # db_connection = init_db()
        mycursor = mysql.connection.cursor()
        val = request.form['name']
        # check if the name already exist in the database
        sql = """SELECT * FROM Username WHERE name=%s"""
        mycursor.execute(sql, val)
        if mycursor.fetchone():
            return "name already exist"
        # execute: insert 'name' into 'Username' table
        sql = """INSERT INTO Username (name) VALUES (%s)"""
        mycursor.execute(sql, val)
        mysql.connection.commit()
        mycursor.close()

    except:
       # return jsonify({'name' : Uname})
        return "Hello" + " " + Uname


# update a username in the 'Username' table in the database 
#@app.route('/hello/<name>', methods = ['PUT'])
@app.route('/hello', methods = ['PUT'])
def putusername(name):
    Uname = request.form['name']
    try:
        #conn = init_db()
        mycursor = mysql.connection.cursor()
        Uname = request.args.get("name")
    # execute: update the 'name' of the wanted username ('name') in the 'Username' table
        sql = """UPDATE Username SET name = %s WHERE id = %s"""
        val = Uname
        mycursor.execute(sql, val)
        msg = "the name was updated."
        mysql.connection.commit()
        mycursor.close()
    except:
        return "db error", 500
    else:
        return "Hello" + " " + Uname + msg

# check if connection to the database established successfully
@app.route('/health', methods=['GET'])
def health():
    try:
        #conn = init_db()
        mycursor = mysql.connection.cursor()
        mycursor.execute("show tables")
        res = str(mycursor.fetchall())
        mysql.connection.commit()
        mycursor.close()
    except:
        return "failed connecting to the database", 500
    else:
        return render_template('health.html', msg=res), 200

if __name__ == "__main__":
    main(debug=True)