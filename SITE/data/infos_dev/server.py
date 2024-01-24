import sqlite3 as sql

class AuthError(Exception):
    def __init__(self):
        super().__init__("Identifiant ou Mot de passe incorrect.")

    

db = sql.connect("DB_MAIN.db")
cur = db.cursor()

cur.execute("SELECT * FROM sqlite_master WHERE type='table';")

tables = cur.fetchall()

def connexion(identifiant:str, mdp:str):
    cur.execute(f"SELECT password FROM users WHERE username = '{identifiant}' ")
    motsdepasse = cur.fetchone()
    if mdp in motsdepasse:
        return True
    else:
        raise AuthError()

print(connexion('rlothore', 'ababb'))


while True:
    pass