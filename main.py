from tools.insert import *
from tools.display import *
import psycopg2
import psycopg2.extras 


def creatView(cur):
    req = f"CREATE OR REPLACE VIEW PopDepartement AS \
        SELECT Departement.IdDepartement, Departement.NameDepartement, Statistic.StartYear, SUM(Statistic.StatValue) as Population \
        FROM Statistic \
            JOIN Communes on Communes.CodeCommune = statistic.CodeCommune \
            JOIN Departement on Communes.IdDepartement = Departement.IdDepartement \
        WHERE Statistic.Indicator = 'Population' \
        AND Statistic.Category LIKE 'Population en %' \
        GROUP BY Departement.IdDepartement, Departement.NameDepartement, Statistic.StartYear;"
    sqlRequest(cur,req)




def getDeptOfRegion(cur,name):
    req = f"SELECT IdDepartement as code_de_departement ,NameDepartement as departement  \
        FROM Region \
        INNER JOIN Departement ON Region.IdRegion = Departement.IdRegion \
        WHERE Region.NameRegion = '{name}' ;"
    selectAndDisplay(cur,req,['code_de_departement','departement'],("All Departement of "+name))

def makeListFromRequest(cur,request,column):
    sqlRequest(cur,request)
    rows = cur.fetchall()
    res = []
    for l in rows: 
        res.append(l[column])
    return res



def _listDeptOfRegion(cur):
    req = f'SELECT IdRegion as code_de_region, NameRegion as region \
        from Region;'
    # selectAndDisplay(cur,req,['code_de_region','region'], "Region list" )
    regionList = makeListFromRequest(cur,req,'region')
    while True : 
        user = getChoice("\t\t  ... Region menu ... " , ['Go to Main menu ','List all region','List departments of...'])
        if user == 1 :
            return 
        elif user == 2 :
            selectAndDisplay(cur,req,['code_de_region','region'], "Region list" )
        elif user == 3 :
            rId = getChoice ("Please choose a Region form this list : ",regionList)
            getDeptOfRegion(cur,regionList[rId-1])

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


def _listCommuneOfDept(cur):
    req = f'SELECT IdDepartement as code_de_departement, NameDepartement as departement \
        from Departement;'
    # selectAndDisplay(cur,req,['code_de_region','region'], "Region list" )
    deptList = makeListFromRequest(cur,req,'departement')
    while True : 
        user = getChoice("\t\t  ... Departement menu ... " , ['Go to Main menu ','List all departement','Get Commune where Population >= ...'])
        if user == 1 :
            return 
        elif user == 2 :
            selectAndDisplay(cur,req,['code_de_departement','departement'], "Departement list" )
        elif user == 3 :
            deptChoice =  getChoice ("Please choose a departement form this list : ",deptList)
            limit = int(input("Please enter the min Population of the Commune : "))
            year = ['2008','2013','2019']
            yearCh =  getChoice ("Please choose a year : ",year)
            deptName = deptList[deptChoice-1].replace("'", "''") # escape single quotes
            deptID = makeListFromRequest(cur, f"SELECT IdDepartement FROM Departement WHERE NameDepartement = '{deptName}'", 0)[0]
            getCommuneOfDept(cur,deptID,deptList[deptChoice-1],limit,year[yearCh-1])

def insertAll(conn , cur):
    printAction('Fill tables...')
    printAction('please wait... ')
    fillScript(conn,cur)
    printAction('End fill tables')


if __name__ == "__main__" :
    printCheers("\t\t>>>>> Welcome to postState <<<<<")
    conn = connect(DBNAME,USERNAME,PASS)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # insertAll(conn , cur)

    while True :
        user = getChoice("\t\t  ... Main menu ... " , ['exit','Region','Get Population of a gaven Department'])
        if user == 1:
            printCheers("\nGoodbye thank you for using our postState app...")
            break
        if user == 2:
           _listDeptOfRegion(cur)
        elif user == 3 :
            _listCommuneOfDept(cur)
        
        
    # selectAndDisplay(cur,"select * from DeptChefLieu;",getLower(TABLE_COLUMNS['DeptChefLieu']))

    # selectAndDisplay(cur,"select * from Statistic;",getLower(TABLE_COLUMNS['Statistic_POP']), "Statistic Table" )

    # selectAndDisplay(cur,"select * from DeptChefLieu;",getLower(TABLE_COLUMNS['DeptChefLieu']))

