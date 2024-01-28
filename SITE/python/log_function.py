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



                   ##    ######   ########  ######  ##   ##   ######   #####                              ##   ##     ##    #######   #####    #####
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

from datetime import datetime
import sqlite3 as sql

###############################################s
##############  DB CONNEXION  ################# 
###############################################

db = sql.connect("data\databases\logs.db")
cur = db.cursor()

###############################################
################  FUNCTION  ################### 
###############################################

def log_action(IdAntenne: int, IdUser : int, action : str):
    """Ajoute une nouvelle entrée à la table des logs de la database 

    Args:
        IdAntenne (int): Identifiant représentant l'antenne dont provient l'action (Ex: Montaigu -> MTGU85 )
        IdUser (int): Identifiant représentant le compte utilisé pour l'action
        action (str): Action effectuée par l'utilisateur
    """

    # Récupération de la date pour la requête SQL finale
    today = datetime.now()
    date = today.strftime("%d/%m/%Y")

    # Récupération de l'heure de l'action
    nowTime = datetime.now()
    heure, min, sec = nowTime.hour, nowTime.minute, nowTime.second
    nowTime = f"{heure}:{min}:{sec}"

    # Récupération du nombre de lignes déja incrites dans les logs pour la requête SQL finale
    cur.execute(f"SELECT COUNT(*) FROM logs_{IdAntenne}")
    entryId = cur.fetchone()[0] + 1

    # Requête SQL finale
    cur.execute(f'INSERT INTO logs_{IdAntenne} VALUES ({entryId}, "{date}", "{nowTime}", {IdUser}, "{action}")')

log_action("MTGU85", 131207, "Created Automatic Logs CODE")

# Exécution des modifications apportées à la database
db.commit()
# Fermeture de la connexion avec la database
db.close()