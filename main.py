from tools.insert import *
from tools.display import *
import psycopg2
import psycopg2.extras 


def _optionRegion(cur):
    req = f'SELECT IdRegion as code_de_region, NameRegion as region \
        from Region;'
    # selectAndDisplay(cur,req,['code_de_region','region'], "Region list" )
    regionList = makeListFromRequest(cur,req,'region')
    year = ['2008','2013','2019']
    while True : 
        user = getChoice("\t\t  ... Region menu ... " , ['Go to Main menu ','List all region','The Most Populated Region','The Least Populated Region','The statistics of births','List departments of...'])
        if user == 1 :
            return 
        elif user == 2 :
            selectAndDisplay(cur,req,['code_de_region','region'], "Region list" )
        elif user == 3 : 
            yearCh =  getChoice ("Please choose a year : ",year)
            getMostLeastRegion(cur,year[yearCh-1],True)
        elif user == 4 : 
            yearCh =  getChoice ("Please choose a year : ",year)
            getMostLeastRegion(cur,year[yearCh-1],False)
        elif user == 5 :
            periodList = getNaissancesPeriodsList(cur)
            periodChoice = getChoice ("Please choose a period form this list : ",periodList)
            strt , end = getPeriodFromCategory(periodList[periodChoice-1])
            getNaissanceRegion(cur,strt,end)
        elif user == 6 :
            rId = getChoice ("Please choose a Region form this list : ",regionList)
            getDeptOfRegion(cur,regionList[rId-1])



def _optionDepartement(cur):
    req = f'SELECT IdDepartement as code_de_departement, NameDepartement as departement \
        from Departement;'
    # selectAndDisplay(cur,req,['code_de_region','region'], "Region list" )
    deptList = makeListFromRequest(cur,req,'departement')
    year = ['2008','2013','2019']

    while True : 
        user = getChoice("\t\t  ... Departement menu ... " , ['Go to Main menu ','List All Departement','The Most Populated Departement','The Least Populated Departement','The statistics of births','Get Communes where Population >= ...'])
        if user == 1 :
            return 
        elif user == 2 :
            selectAndDisplay(cur,req,['code_de_departement','departement'], "Departement list" )
        elif user == 3 : 
            yearCh =  getChoice ("Please choose a year : ",year)
            getMostLeastDept(cur,year[yearCh-1],True)
        elif user == 4 : 
            yearCh =  getChoice ("Please choose a year : ",year)
            getMostLeastDept(cur,year[yearCh-1],False)
        elif user == 5 :
            periodList = getNaissancesPeriodsList(cur)
            periodChoice = getChoice ("Please choose a period form this list : ",periodList)
            strt , end = getPeriodFromCategory(periodList[periodChoice-1])
            getNaissanceDept(cur,strt,end)
        elif user == 6 :
            deptChoice =  getChoice ("Please choose a departement form this list : ",deptList)
            limit = int(input("Please enter the min Population of the Commune : "))
            yearCh =  getChoice ("Please choose a year : ",year)
            deptName = deptList[deptChoice-1].replace("'", "''") # escape single quotes
            deptID = makeListFromRequest(cur, f"SELECT IdDepartement FROM Departement WHERE NameDepartement = '{deptName}'", 0)[0]
            getCommuneOfDept(cur,deptID,deptList[deptChoice-1],limit,year[yearCh-1])


if __name__ == "__main__" :
    printCheers("\t\t>>>>> Welcome to postState <<<<<")
    conn = connect(DBNAME,USERNAME,PASS)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # insertAll(conn , cur)
    # Vues : 
    creatPopDeptView(cur)
    creatPopRegionView(cur)
    creatNaissancesDeptView(cur)
    creatNaissancesRegionView(cur)

    while True :
        user = getChoice("\t\t  ... Main menu ... " , ['exit','Region','Department'])
        if user == 1:
            printCheers("\nGoodbye thank you for using our postState app...")
            break
        if user == 2:
           _optionRegion(cur)
        elif user == 3 :
            _optionDepartement(cur)
        elif user == 4 : 
            pass
        
        
    # selectAndDisplay(cur,"select * from DeptChefLieu;",getLower(TABLE_COLUMNS['DeptChefLieu']))

    # selectAndDisplay(cur,"select * from Statistic;",getLower(TABLE_COLUMNS['Statistic_POP']), "Statistic Table" )

    # selectAndDisplay(cur,"select * from DeptChefLieu;",getLower(TABLE_COLUMNS['DeptChefLieu']))

