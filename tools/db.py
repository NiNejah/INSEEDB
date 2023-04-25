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
        exit(color.RED +"Error when try to get "+ cmd +": \n" + str(e)+color.END)

def selectAndDisplay(cur,request,columns,description = ''):
    print (color.GREEN +"\n\t\t... "+description+" ... ")
    sqlRequest(cur,request)
    rows = cur.fetchall()
    res = tableToString(rows,columns)
    print(res+color.END)

def makeListFromRequest(cur,request,column):
    sqlRequest(cur,request)
    rows = cur.fetchall()
    res = []
    for l in rows: 
        res.append(l[column])
    return res



###################  Region ###################

def getDeptOfRegion(cur,name):
    req = f"SELECT IdDepartement as code_de_departement ,NameDepartement as departement  \
        FROM Region \
        INNER JOIN Departement ON Region.IdRegion = Departement.IdRegion \
        WHERE Region.NameRegion = '{name}' ;"
    selectAndDisplay(cur,req,['code_de_departement','departement'],("All Departement of "+name))

def creatPopRegionView(cur):
    req = f"CREATE OR REPLACE VIEW PopRegion AS \
        SELECT Region.IdRegion, Region.NameRegion, Statistic.StartYear, SUM(Statistic.StatValue) as Population \
        FROM Departement \
            JOIN Region ON Region.IdRegion = Departement.IdRegion \
            JOIN Commune ON Departement.IdDepartement = Commune.IdDepartement \
            JOIN Statistic ON Statistic.CodeCommune = Commune.CodeCommune \
        WHERE Statistic.Indicator = 'Population' \
        AND Statistic.Category LIKE 'Population en %' \
        GROUP BY Region.IdRegion, Region.NameRegion, Statistic.StartYear;"
    sqlRequest(cur,req)

def getMostLeastRegion(cur,year,most):
    req = f"SELECT IdRegion as code_region, NameRegion as region, population FROM PopRegion \
            WHERE StartYear = {year}"
    title = ''
    if(most):
        req += "ORDER BY Population DESC LIMIT 1;"
        title  = "The Most Populated Region "
    else :
        req += "ORDER BY Population ASC LIMIT 1;"
        title  = "The Least Populated Region "
    selectAndDisplay(cur,req,['code_region','region','population'], title )

def creatNaissancesRegionView(cur):
    req = f"CREATE OR REPLACE VIEW NaissRegion AS \
        SELECT Region.IdRegion, Region.NameRegion, Statistic.StartYear, Statistic.EndYear, SUM(Statistic.StatValue) as RNaissance \
        FROM Departement \
            JOIN Region ON Region.IdRegion = Departement.IdRegion \
            JOIN Commune ON Departement.IdDepartement = Commune.IdDepartement \
            JOIN Statistic ON Statistic.CodeCommune = Commune.CodeCommune \
        WHERE Statistic.Indicator = 'Naissances' \
        AND Statistic.Category LIKE 'Naissances entre %' \
        GROUP BY Region.IdRegion, Region.NameRegion, Statistic.StartYear, Statistic.EndYear;"
    sqlRequest(cur,req)
  

def getNaissanceRegion(cur,startYear,endYear):
    req = f"SELECT NameRegion as region , SUM(RNaissance) as total_naissance \
        FROM NaissRegion \
        WHERE StartYear = {startYear} AND EndYear = {endYear} \
        GROUP BY region \
        ORDER BY total_naissance DESC;"
    selectAndDisplay(cur,req,['region','total_naissance',], f"The statistics of births in French region betwin {startYear} - {endYear} from the most to the least")


################### Departement ###################

def getCommuneOfDept(cur,IdDept,NameDept,minPop,year):
    req = f"SELECT Commune.NameCommune as commune , Statistic.StatValue as population \
        FROM Commune \
        INNER JOIN Statistic ON Commune.CodeCommune = Statistic.CodeCommune \
        WHERE Commune.IdDepartement  = '{IdDept}'  \
        AND Indicator = 'Population'  \
        AND Category LIKE 'Population en %' \
        AND StartYear = {year} \
        AND EndYear IS NULL \
        AND Statistic.StatValue >= {minPop};"
    selectAndDisplay(cur,req,['commune','population'], "Populasion of "+NameDept )

def creatPopDeptView(cur):
    req = f"CREATE OR REPLACE VIEW PopDepartement AS \
        SELECT Departement.IdDepartement, Departement.NameDepartement, Statistic.StartYear, SUM(Statistic.StatValue) as Population \
        FROM Statistic \
            JOIN Commune on Commune.CodeCommune = statistic.CodeCommune \
            JOIN Departement on Commune.IdDepartement = Departement.IdDepartement \
        WHERE Statistic.Indicator = 'Population' \
        AND Statistic.Category LIKE 'Population en %' \
        GROUP BY Departement.IdDepartement, Departement.NameDepartement, Statistic.StartYear;"
    sqlRequest(cur,req)

def getMostLeastDept(cur,year,most):
    req = f"SELECT IdDepartement as code_department, NameDepartement as departement, population FROM PopDepartement \
            WHERE StartYear = {year}"
    title = ''
    if(most):
        req += "ORDER BY Population DESC LIMIT 1"
        title  = "The Most Populated Departement "
    else :
        req += "ORDER BY Population ASC LIMIT 1"
        title  = "The Least Populated Departement "
    selectAndDisplay(cur,req,['code_department','departement','population'], title )

def creatNaissancesDeptView(cur):
    req = f"CREATE OR REPLACE VIEW NaissDepartement AS \
        SELECT Departement.IdDepartement, Departement.NameDepartement, Statistic.StartYear,  Statistic.EndYear, SUM(Statistic.StatValue) as Naissance \
        FROM Statistic \
            JOIN Commune on Commune.CodeCommune = statistic.CodeCommune \
            JOIN Departement on Commune.IdDepartement = Departement.IdDepartement \
        WHERE Statistic.Indicator = 'Naissances' \
        AND Statistic.Category LIKE 'Naissances entre %' \
        GROUP BY Departement.IdDepartement, Departement.NameDepartement, Statistic.StartYear, Statistic.EndYear;"
    sqlRequest(cur,req)

def getNaissanceDept(cur,startYear,endYear):
    req = f"SELECT NameDepartement as departement, SUM(Naissance) as total_naissance \
        FROM NaissDepartement \
        WHERE StartYear = {startYear} AND EndYear = {endYear} \
        GROUP BY departement \
        ORDER BY total_naissance DESC;"
    selectAndDisplay(cur,req,['departement','total_naissance',], f"The statistics of births in French departments betwin {startYear} - {endYear} from the most to the least")



def getNaissancesPeriodsList(cur):
    req = f"SELECT DISTINCT Category as period FROM Statistic \
            WHERE Indicator = 'Naissances' \
            ORDER BY period ASC;"
    return makeListFromRequest(cur,req,'period')

