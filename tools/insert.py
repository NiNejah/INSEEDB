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
        try :
            cur.copy_from(csvfile, table, sep=sep, columns=columns)
        except Exception as e : 
            exit("\033[91mcopy_from exception : " + str(e))


def fillPopulation2(cur):
    year = ['_08','_13','_19']
    sex = ['','_F','_H']
    period = ['','_00_14','_15_29','_30_44','_45_59','_60_74','_75_89','_90_plus']
    for y in year : 
        for p in period :
            for s in sex:
                print(fileFile+'pop/Population'+y+p+s+'.csv')
                fillTable(fileFile+'pop/Population'+y+p+s+'.csv',"statistic",cur,getLower(TABLE_COLUMNS['Statistic_POP']),sep=';')

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

def fillScript(conn,cur):
    fillTable(fileFile+'fill_region.csv',"region",cur,getLower(TABLE_COLUMNS['Region']),sep=',')
    fillTable(fileFile+'fill_departement.csv',"departement",cur,getLower(TABLE_COLUMNS['Departement']),sep=',')
    fillTable(fileFile+'fill_commune.csv',"commune",cur,getLower(TABLE_COLUMNS['Commune']),sep=',')
    fillTable(fileFile+'fill_region_chefLieu.csv',"regioncheflieu",cur,getLower(TABLE_COLUMNS['RegionChefLieu']),sep=',')
    fillTable(fileFile+'fill_departement_chefLieu.csv',"deptcheflieu",cur,getLower(TABLE_COLUMNS['DeptChefLieu']),sep=',')
    # fillTable(fileFile+'pop/test/Population_19.csv',"statistic",cur,getLower(TABLE_COLUMNS['Statistic']),sep=';')
    fillStat(cur)
    conn.commit()

def insertAll(conn , cur):
    printAction('Fill tables...')
    printAction('please wait... ')
    fillScript(conn,cur)
    printAction('End fill tables')
