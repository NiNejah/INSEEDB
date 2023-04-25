import os
from tools.db import *

# For the code refactoring.
TABLE_COLUMNS = {
    'Region' : ['IdRegion' , 'NameRegion'],
    'Departement': ['IdDepartement','IdRegion','NameDepartement'],
    'Commune' : ['CodeCommune','IdDepartement','NameCommune'],
    'RegionChefLieu' :  ['IdRegion','CodeCommune'],
    'DeptChefLieu' :  ['IdDepartement','CodeCommune' ],
    'Statistic_POP' : ['CodeCommune','Indicator','Category','StartYear','StatValue'],
    'Statistic_NAISS' : ['CodeCommune','Indicator','Category','StartYear','EndYear','StatValue']
}

# path to the directory where the CSV files are stored
FILE_PATH = "./csv/fill/"

# This function that converts all strings in a list to lowercase
def getLower(myList):
    res = []
    for i in range(len(myList)):
        res.append(myList[i].lower())
    return res 

# This function reads a CSV file and inserts its data into a PostgreSQL table
def fillTable(file, table, cur, columns, sep=';'):
    with open(file, 'r') as csvfile:
            cur.copy_from(csvfile, table, sep=sep, columns=columns)

# This function inserts the data from the population CSV files into the "statistic" table
def fillPopulation(cur):
    for filename in os.listdir(FILE_PATH+'/pop/'):
        if not filename.endswith('.csv'):
            continue 
         # call the fillTable function to insert the data from the CSV file
        fillTable(FILE_PATH+'/pop/'+filename,"statistic",cur,getLower(TABLE_COLUMNS['Statistic_POP']),sep=';')

# This function inserts the data from the birth CSV files into the "statistic" table
def fillNaissances(cur):
    for filename in os.listdir(FILE_PATH+'/naiss/'):
        if not filename.endswith('.csv'):
            continue 
        # print(filename)
        fillTable(FILE_PATH+'/naiss/'+filename,"statistic",cur,getLower(TABLE_COLUMNS['Statistic_NAISS']),sep=';')

# This function calls the fillPopulation and fillNaissances functions to insert all the data into the "statistic" table
def fillStat(cur):
    fillPopulation(cur)
    fillNaissances(cur)

# This insert all the data into the "Region","Departement" ,"Commune","DeptChefLieu","DeptChefLieu" and "statistic" tables, 
def fillScript(cur):
    fillTable(FILE_PATH+'fill_region.csv',"region",cur,getLower(TABLE_COLUMNS['Region']),sep=',')
    fillTable(FILE_PATH+'fill_departement.csv',"departement",cur,getLower(TABLE_COLUMNS['Departement']),sep=',')
    fillTable(FILE_PATH+'fill_commune.csv',"commune",cur,getLower(TABLE_COLUMNS['Commune']),sep=',')
    fillTable(FILE_PATH+'fill_region_chefLieu.csv',"regioncheflieu",cur,getLower(TABLE_COLUMNS['RegionChefLieu']),sep=',')
    fillTable(FILE_PATH+'fill_departement_chefLieu.csv',"deptcheflieu",cur,getLower(TABLE_COLUMNS['DeptChefLieu']),sep=',')
    fillStat(cur)
    
# This function inserts all the data into the PostgreSQL database
# with handling the unique constraint violation '23505' error code 
def insertAll(conn , cur):
    try :
        printAction('Fill tables...')
        printAction('please wait... ')
        fillScript(cur)
        conn.commit()
        printAction('End fill tables, Please commante this line : insertAll(conn , cur) in main.py')
    except psycopg2.Error as e :
            # if the error code is '23505', which indicates a key violation (unique constraint violation), 
            # rollback the transaction and print a message informing the user that they have already inserted all the files
            if e.pgcode == '23505':
                conn.rollback()  # rollback the transaction
                print(color.RED +"You have already inserted all file please make sour that you commented this line : insertAll(conn,cut) in main.py")
            else:
                # if the error is not a key violation, close the cursor and exit the program with an error message
                cur.close()
                exit(color.RED+"copy_from exception : " + str(e)+color.END)