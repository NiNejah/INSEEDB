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

def fillTable(file, table, cur, columns, sep=';'):
    with open(file, 'r') as csvfile:
        try :
            cur.copy_from(csvfile, table, sep=sep, columns=columns)
        except Exception as e : 
            exit("copy_from exception : " + str(e))

def sqlRequest(conn, cur, cmd):
    try:
        cur.execute("""
        %s
        """,(cmd))
    except Exception as e :
        #fermeture de la connexion
        cur.close()
        conn.close()
        exit("error when try to get : "+cmd + " e : " + str(e))
 
def toString(rows , rosName):
    page = rosName[0] + ' | '+ rosName[1] + '\n'
    for d in rows :
        page += str(d[rosName[0]])+" : "+str(d[rosName[1]])+"\n"
    return page

if __name__ == "__main__" :
    print ("welcome to postState ...")
    conn = connect(DBNAME,USERNAME,PASS)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    fillTable('./csv/fill_region.csv',"region",cur,['idregion' , 'nomregion'],sep=',')
    cur.execute("select * from region;")
    rows = cur.fetchall()
    res = toString(rows,['idregion','nomregion'])
    print(res)
    fillTable('./csv/fill_region_chef.csv',"regioncheflieu",cur,['idregion' , 'idcommune'],sep=',')
    cur.execute("select * from regioncheflieu;")
    rows = cur.fetchall()
    res = toString(rows,['idregion','idcommune'])
    print(res)




