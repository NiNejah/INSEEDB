from tools.insert import *
from tools.color import color 
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
        exit(color.RED +"Connexion impossible à la base de données: " + str(e) +color.END) 

def sqlRequest(conn, cur, cmd):
    try:
        cur.execute("""from tools.config import *
        %s
        """,(cmd))
    except Exception as e :
        #fermeture de la connexion
        cur.close()
        conn.close()
        exit(color.RED +"error when try to get : "+cmd + " e : " + str(e)+color.END)
 
def toString(rows , rowsName):
    page ='\n'
    for r in rowsName : 
        page += f'{r:15} |'
    page = page[:-1] + '\n'
    for i in range (len(rowsName)):
        page += "----------------|"
    page = page[:-1] + '\n'
    for d in rows :
        for r in rowsName :
            s = str(d[r])
            page += f'{s:15} |'
        page = page[:-1] + '\n'
    return page

if __name__ == "__main__" :
    print ("\033[93mWelcome to postState ")
    conn = connect(DBNAME,USERNAME,PASS)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    filleScript(cur)
    cur.execute("select * from Region;")
    rows = cur.fetchall()
    res = toString(rows,getLower(TABLE_COLUMNS['Region']))
    print(color.GREEN+res+color.END)
    # cur.execute("select * from commune;")
    # rows = cur.fetchall()
    # res = toString(rows,getLower(TABLE_COLUMNS['Commune']))
    # print(color.GREEN+res+color.END)
