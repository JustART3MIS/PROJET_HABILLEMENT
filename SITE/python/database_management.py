####################################################################################################################################################################

    ######   ######    #####    ######  #######   #####    ######   ######   #####   ##  ###            #####    ######  ### ###   ######  ###      #######
    ### ###  ### ###  ### ###   # ## #  ### ###  ### ###   # ## #     ##    ### ###  ### ###           ### ###     ##    ### ###     ##    ###      ### ###
    ### ###  ### ###  ### ###     ##    ###      ###         ##       ##    ### ###  #######           ###         ##    ### ###     ##    ###      ###
    ######   ######   ### ###     ##    #####    ###         ##       ##    ### ###  #######           ###         ##    ### ###     ##    ###      #####
    ###      ### ##   ### ###     ##    ###      ###         ##       ##    ### ###  ### ###           ###         ##    ### ###     ##    ###      ###
    ###      ### ###  ### ###     ##    ### ###  ### ###     ##       ##    ### ###  ### ###           ### ###     ##     #####      ##    ###  ##  ### ###
    ###      ### ###   #####      ##    #######   #####      ##     ######   #####   ### ###            #####    ######    ###     ######  #######  #######



                                     ##  ##  #######  ##   ##  ######   #######  #######         ##   ####    ######   ##
                                     ##  ##   ##  ##  ###  ##   ##  ##   ##  ##   ##  ##        ##   ##  ##   ##  ##    ##
                                     ##  ##   ##      #### ##   ##  ##   ##       ##            ##   ##  ##   ##        ##
                                     ##  ##   ####    ## ####   ##  ##   ####     ####          ##    ####    #####     ##
                                     ##  ##   ##      ##  ###   ##  ##   ##       ##            ##   ##  ##       ##    ##
                                      ####    ##  ##  ##   ##   ##  ##   ##  ##   ##  ##        ##   ##  ##   ##  ##    ##
                                       ##    #######  ##   ##  ######   #######  #######         ##   ####     ####    ##



                   ##    ######   ########  ######  ##   ##   ######   #####                  ##          ##   ##     ##    #######   #####    #####
                  ####    ##  ##  #  ##  #     ##   ### ###     ##    ##   ##                ##           ###  ##    ####    ##  ##  ##   ##  ##   ##
                 ##  ##   ##  ##     ##       ##    #######     ##    ##                    ##            #### ##   ##  ##   ##      ##       ##   ##
                 ######   #####      ##        ##   ## # ##     ##     #####               ##             ## ####   ######   ####     #####   ##   ##
                 ##  ##   ####       ##         ##  ##   ##     ##         ##             ##              ##  ###   ##  ##   ##           ##  ##   ##
                 ##  ##   ## ##      ##     ##  ##  ##   ##     ##    ##   ##            ##               ##   ##   ##  ##   ##  ##  ##   ##  ##   ##
                 ##  ##  ###  ##    ####     ####   ##   ##   ######   #####            ##                ##   ##   ##  ##  #######   #####    #####



####################################################################################################################################################################

    ###############################################
    #################  IMPORTS  ################### 
    ###############################################

import sqlite3 as sql
from tabulate import tabulate
from unidecode import unidecode


    ###############################################
    ##############  DB CONNEXION  ################# 
    ###############################################

DB_PRINCIPALE = sql.connect("site\data\databases\DB_MAIN.db")
DB_USERS = sql.connect("site\data\databases\profiles.db")

cur = DB_PRINCIPALE.cursor()
users = DB_USERS.cursor()

    ################################################
    ################  FUNCTIONS  ################### 
    ################################################

def verif_connexion(db_cursor):
    """Vérifie si la connexion à bien été effectuée en listant les tables de la database
    
    Renvoi :
        str : Listes des tables"""

    # Requête pour obtenir les noms de toutes les tables dans la base de données
    db_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Récupérer les résultats de la requête
    tables = db_cursor.fetchall()

    # Afficher les noms des tables
    if tables:
        renvoi = "Tables existantes dans la base de données :"
  
        for table in tables:
            renvoi += "\n"
            renvoi += str(table[0])
        renvoi += "\n ------------ \n"
    else:
        renvoi = "Aucune table trouvée dans la base de données."
    
    return renvoi

def add_account(permission_lvl, username, password):
    if permission_lvl == 1 : # Identifiants d'Antenne
        users.execute(f"INSERT INTO users(username, pwd_reference) VALUES ({username}, "")")

    elif permission_lvl == 3: # Admins
        users.execute(f"INSERT INTO admins(username, pwd_reference) VALUES ({username}, {password})")

    elif permission_lvl == 4: # Superadmins
        users.execute(f"INSERT INTO superadmins(username, pwd_reference) VALUES ({username}, {password})")

def add_referent(nom, prenom, antenne, pwd):
   users.execute(f'INSERT INTO referents(username, pwd_reference) VALUES ("{nom[0]}.{prenom}_{antenne}", "{pwd}")')



def change_pwd():
    pass

def voir_vetements(id_antenne:str, id_vetement:str = None , statut:str = None):
    """Affiche la sélection souhaitée de vêtements de la table SQL dans un format lisible dans une console

    Paramètres :
        id_antenne (str): _description_
        id_vetement (str, optional): _description_. Par défaut à None.
        statut (str, optional): _description_. Par défaut à None.

    Renvoi :
        str: Tableau mis en forme pour une console
    """
    
    if id_vetement != None:
        id_antenne = unidecode(id_antenne)
        cur.execute(f"SELECT * FROM VETEMENTS_{id_antenne} WHERE n_inventaire = {id_vetement};")
        vetements = cur.fetchall()

    elif statut != None:
        statut = unidecode(statut)
        cur.execute(f"SELECT * FROM VETEMENTS_{id_antenne} WHERE statut LIKE '%{statut}%' ;")
        vetements = cur.fetchall()

    else:
        cur.execute(f"SELECT * FROM VETEMENTS_{id_antenne};")
        vetements = cur.fetchall()

    # Convertir les tuples en listes
    for index in range(len(vetements)):
        nouvelle_liste = []

        for contenu in vetements[index]:
            nouvelle_liste.append(contenu)

    # En-têtes de l'affichage correspondant a chacune des cles de la table SQL
    headers = ["Type", "Quantité", "Section", "Modele", "N° Serie", "Statut", "Date Limite", "N° Inventaire", "Lieu Stockage", "Commentaire", "Année", "Affectation",]

    # Utilisez la fonction tabulate pour afficher le tableau avec les en-têtes
    table = tabulate(vetements, headers, tablefmt="simple")

    # Renvoi de l'affichage de la table
    return table

def ajouter_vetement(idAntenne:str, type:str, quantite:int = 1, modele:str = None, numero_serie:str = None, statut:str = None, date_limite:str = None,
                     numero_inventaire:int = None, lieu_stockage:str = None, commentaire:str = None, annee:int = None, affectation:str = None):
    
    # Créer un dictionnaire des paramètres avec leurs valeurs par défaut
    defaults = {'modele': modele, 'numero_serie': numero_serie, 'statut': statut, 'date_limite': date_limite,
                'numero_inventaire': numero_inventaire, 'lieu_stockage': lieu_stockage, 'commentaire': commentaire,
                'annee': annee, 'affectation': affectation}
    
    # Remplacer les valeurs None par 'NULL' dans le dictionnaire des paramètres par défaut
    for param, value in defaults.items():
        if value is None:
            defaults[param] = 'NULL'
        else:
            defaults[param] = f"'{value}'"  # Entourer les valeurs avec des guillemets
    
    # Exécuter la requête SQL en utilisant les valeurs modifiées
    cur.execute(f"""INSERT INTO [VETEMENTS_{idAntenne}] VALUES('{type}', '{quantite}', '{idAntenne}', {defaults['modele']},
                {defaults['numero_inventaire']}, {defaults['statut']}, {defaults['date_limite']}, {defaults['numero_inventaire']},
                {defaults['lieu_stockage']}, {defaults['commentaire']}, {defaults['annee']}, {defaults['affectation']})""")

print(verif_connexion(users))

# Applique toutes les modifications effectuées à la Database
DB_PRINCIPALE.commit()

# Ferme la connexion avec la database
DB_PRINCIPALE.close()
