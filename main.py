from config import *

import psycopg2
import psycopg2.extras 
import csv 


# connect to an existing database
def connect(dbName , userName , Pass):
    print('Connexion à la base de données...')
    try:
        conn = psycopg2.connect("host=localhost dbname="+dbName+" user="+userName+" password="+Pass)
        return conn ; 
    except Exception as e :
        exit("Connexion impossible à la base de données: " + str(e)) 


if __name__ == "__main__" : 
    print ("welcome to postState ...")
    conn = connect(DBNAME,USERNAME,PASS)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    df = csv('v_region_2023.csv')
    print(df)
    # try: 
    #     cur.copy_from(df,"Region",sep=',',columns=('IdRegion','NomRegion'))
    # except Exception as e :
    #     exit("copy_from exception : " + str(e))




