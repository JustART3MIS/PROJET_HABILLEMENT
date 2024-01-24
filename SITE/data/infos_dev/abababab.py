import sqlite3 as sql

db = sql.connect("DB_MAIN.db")
cur = db.cursor()


cur.execute("SELECT password FROM users WHERE username = 'ababa' ")
true_password = str(cur.fetchone()[0])

print(true_password)