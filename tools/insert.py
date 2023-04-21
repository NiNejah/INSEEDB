from typing import List
from tools.config import *

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


def filleScript(cur):
    fillTable('./csv//fill/fill_region.csv',"region",cur,getLower(TABLE_COLUMNS['Region']),sep=',')
    fillTable('./csv//fill/fill_departement.csv',"departement",cur,getLower(TABLE_COLUMNS['Departement']),sep=',')
    fillTable('./csv//fill/fill_commune.csv',"commune",cur,getLower(TABLE_COLUMNS['Commune']),sep=',')
    fillTable('./csv/fill/fill_region_chefLieu.csv',"regioncheflieu",cur,getLower(TABLE_COLUMNS['RegionChefLieu']),sep=',')
    fillTable('./csv/fill/fill_departement_chefLieu.csv',"deptcheflieu",cur,getLower(TABLE_COLUMNS['DeptChefLieu']),sep=',')
