import psycopg2
from tools.display import *

DBNAME = "insee"
USERNAME="postgres"
PASS="1111"

TABLE_COLUMNS = {
    'Region' : ['IdRegion' , 'NameRegion'],
    'Departement': ['IdDepartement','IdRegion','NameDepartement'],
    'Commune' : ['CodeCommune','IdDepartement','NameCommune'],
    'RegionChefLieu' :  ['IdRegion','CodeCommune'],
    'DeptChefLieu' :  ['IdDepartement','CodeCommune' ],
    'Statistic_POP' : ['CodeCommune','Indicator','Category','StartYear','StatValue'],
    'Statistic_NAISS' : ['CodeCommune','Indicator','Category','StartYear','EndYear','StatValue']
}


def connect(dbName , userName , Pass):
    printAction('Connecting to database...')
    try:
        conn = psycopg2.connect("host=localhost dbname="+dbName+" user="+userName+" password="+Pass)
        return conn ; 
    except Exception as e :
        exit(color.RED +"Unable to connect to database: " + str(e) +color.END) 


def sqlRequest(cur, cmd):
    try:
        cur.execute(cmd)
    except Exception as e :
        #fermeture de la connexion
        cur.close()
        exit(color.RED +"Error when try to get "+cmd + ": \n" + str(e)+color.END)

def selectAndDisplay(cur,request,columns,description = ''):
    print (color.GREEN +"\n\t\t... "+description+" ... ")
    sqlRequest(cur,request)
    rows = cur.fetchall()
    res = tableToString(rows,columns)
    print(res+color.END)