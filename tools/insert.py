import os
from typing import List
from tools.db import *

fileFile = "./csv/fill/"

def getLower(myList:List[str]):
    res = []
    for i in range(len(myList)):
        res.append(myList[i].lower())
    return res 

def fillTable(file, table, cur, columns, sep=';'):
    with open(file, 'r') as csvfile:
            cur.copy_from(csvfile, table, sep=sep, columns=columns)


def fillPopulation(cur):
    for filename in os.listdir(fileFile+'/pop/'):
        if not filename.endswith('.csv'):
            continue 
        # print(filename)
        fillTable(fileFile+'/pop/'+filename,"statistic",cur,getLower(TABLE_COLUMNS['Statistic_POP']),sep=';')

    # fillTable(fileFile+'Population'+year[2]+'.csv',"statistic",cur,getLower(TABLE_COLUMNS['Statistic']),sep=';')
def fillNaissances(cur):
    for filename in os.listdir(fileFile+'/naiss/'):
        if not filename.endswith('.csv'):
            continue 
        # print(filename)
        fillTable(fileFile+'/naiss/'+filename,"statistic",cur,getLower(TABLE_COLUMNS['Statistic_NAISS']),sep=';')



def fillStat(cur):
    fillPopulation(cur)
    fillNaissances(cur)

def fillScript(cur):
    fillTable(fileFile+'fill_region.csv',"region",cur,getLower(TABLE_COLUMNS['Region']),sep=',')
    fillTable(fileFile+'fill_departement.csv',"departement",cur,getLower(TABLE_COLUMNS['Departement']),sep=',')
    fillTable(fileFile+'fill_commune.csv',"commune",cur,getLower(TABLE_COLUMNS['Commune']),sep=',')
    fillTable(fileFile+'fill_region_chefLieu.csv',"regioncheflieu",cur,getLower(TABLE_COLUMNS['RegionChefLieu']),sep=',')
    fillTable(fileFile+'fill_departement_chefLieu.csv',"deptcheflieu",cur,getLower(TABLE_COLUMNS['DeptChefLieu']),sep=',')
    # fillTable(fileFile+'pop/test/Population_19.csv',"statistic",cur,getLower(TABLE_COLUMNS['Statistic']),sep=';')
    fillStat(cur)
    

def insertAll(conn , cur):
    try :
        printAction('Fill tables...')
        printAction('please wait... ')
        fillScript(cur)
        conn.commit()
        printAction('End fill tables, Please commante this line : insertAll(conn , cur) in main.py')
    except psycopg2.Error as e :
        #fermeture de la connexion
            if e.pgcode == '23505': # check for key violation error code
                conn.rollback()  # rollback the transaction
                print(color.RED +"You have already inserted all file please make sour that you commented this line : insertAll(conn,cut) in main.py")
            else:
                cur.close()
                exit(color.RED+"copy_from exception : " + str(e)+color.END)