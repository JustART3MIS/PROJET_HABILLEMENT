from flask import Flask, render_template, request
import sqlite3 as sql
from time import sleep

db = sql.connect("../data/DB_MAIN.db")
cur = db.cursor()

app = Flask(__name__)

class AuthError(Exception):
    def __init__(self):
        super().__init__("Identifiant ou Mot de passe incorrect.")

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/', methods= ["GET", "POST"])
def connexion():
    if request.method == "POST":
        
        username = request.form.get("username")

        password = request.form.get("password") 

        cur.execute(f"SELECT password FROM users WHERE username = {username} ")

        try :
            true_password = str(cur.fetchone()[0])
        except TypeError:
            render_template('')
            sleep(8)
            return(render_template('login.html'))
        
       
    
        if true_password == password :
                return render_template("main.html")
 
if __name__=='__main__':
   app.run()

Flask.run(app)