import psycopg2
from tools.display import *



def creatDB(conn, cur):
    with open("../sql/tables", 'r') as f:
        sql = f.read()
        cur.execute(sql)
        conn.commit()


def connect(host,dbName , userName , Pass):
    printAction('Connecting to database...')
    try:
        conn = psycopg2.connect("host="+host+" dbname="+dbName+" user="+userName+" password="+Pass)
        return conn 
    except Exception as e :
        exit(color.RED +"Unable to connect to database: " + str(e) +color.END)


def sqlRequest(cur, cmd):
    try:
        cur.execute(cmd)
    except Exception as e :
        #fermeture de la connexion
        cur.close()
        exit(color.RED +"Error when try to get "+ cmd +": \n" + str(e)+color.END)

# cur : the database cursor ,
# request : SQL SELECT command string, 
# columns : list of column names, 
# description : description string.
# The function executes the SELECT command using the cursor, fetches all rows returned by the command,
# and converts them to a string representation using the tableToString function. The resulting string is
# then printed with a green color-coded header indicating the description of the result.
def selectAndDisplay(cur,request,columns,description = ''):
    print (color.GREEN +"\n\t\t... "+description+" ... ")
    sqlRequest(cur,request)
    rows = cur.fetchall()
    res = tableToString(rows,columns)
    print(res+color.END)

# cur : the database cursor ,
# request : SQL SELECT command string, 
# column : column name,
# It executes the SELECT command using the cursor.
# The function then fetches all rows returned by the command, extracts the value of the specified column for each row, 
# and returns a list containing these values.
def makeListFromRequest(cur,request,column):
    sqlRequest(cur,request)
    rows = cur.fetchall()
    res = []
    for l in rows:
        res.append(l[column])
    return res

################### Views ###################
def creatViews(cur):
    creatPopDeptView(cur)
    creatPopRegionView(cur)
    creatNaissancesDeptView(cur)
    creatNaissancesRegionView(cur)

###################  Region ###################

# This function takes a cursor cur and a string name as input.
# It selects the department code and name from the Departement table
# based on the name of the region provided and displays the result using the selectAndDisplay() function.
def getDeptOfRegion(cur,name):
    req = f"SELECT IdDepartement as code_de_departement ,NameDepartement as departement  \
        FROM Region \
        INNER JOIN Departement ON Region.IdRegion = Departement.IdRegion \
        WHERE Region.NameRegion = '{name}' ;"
    selectAndDisplay(cur,req,['code_de_departement','departement'],("All Departement of "+name))

# This function takes a cursor cur as input.
# It creates or replaces a view named PopRegion that retrieves the population
# of each region from the Statistic table and displays it using the selectAndDisplay() function.
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

# This function takes a cursor cur, an integer year, and a boolean most as input.
# It retrieves the most or least populated region in the given year from the PopRegion view and
# displays the result using the selectAndDisplay() function.
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

# This function takes a cursor cur as input.
# It creates or replaces a view named NaissRegion that retrieves the number of births in
# each region from the Statistic table and displays it using the selectAndDisplay() function.
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

# This function takes a cursor cur, two integers startYear and endYear as input.
# It retrieves the statistics of births in French regions between the start and end years
# from the NaissRegion view and displays the result using the selectAndDisplay() function.
def getNaissanceRegion(cur,startYear,endYear):
    req = f"SELECT NameRegion as region , SUM(RNaissance) as total_naissance \
        FROM NaissRegion \
        WHERE StartYear = {startYear} AND EndYear = {endYear} \
        GROUP BY region \
        ORDER BY total_naissance DESC;"
    selectAndDisplay(cur,req,['region','total_naissance',], f"The statistics of births in French region between {startYear} - {endYear} from the most to the least")


################### Departement ###################

# cur : the database cursor,
# a department ID (IdDept), the name of the department (NameDept),
#  a minimum population (minPop), and a year (year).
# It retrieves the names and populations of all communes in the given department that have a
# population greater than or equal to the minimum population in the given year.
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

# cur : the database cursor,
# It creates a view (PopDepartement) that calculates the total population of each department
# for each year in the database.
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

# cur : the database cursor,
# year : StartYear,
# most : boolean .
# If most is True, it retrieves the department with the highest population in the given year.
# Otherwise, it retrieves the department with the lowest population in the given year.
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

# cur : the database cursor,
# It creates a view (NaissDepartement)
# that calculates the total number of births in each department for each year in the database.
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

# cur : the database cursor,
# startYear :start year, 
# endYear : end year (endYear). 
# It retrieves the total number of births in each department 
# between the start year and the end year, and orders them from highest to lowest.
def getNaissanceDept(cur,startYear,endYear):
    req = f"SELECT NameDepartement as departement, SUM(Naissance) as total_naissance \
        FROM NaissDepartement \
        WHERE StartYear = {startYear} AND EndYear = {endYear} \
        GROUP BY departement \
        ORDER BY total_naissance DESC;"
    selectAndDisplay(cur,req,['departement','total_naissance',], f"The statistics of births in French departments between {startYear} - {endYear} from highest to lowest")

# cur : the database cursor,
# It retrieves a list of all time periods for which birth statistics are available in the databa
def getNaissancesPeriodsList(cur):
    req = f"SELECT DISTINCT Category as period FROM Statistic \
            WHERE Indicator = 'Naissances' \
            ORDER BY period ASC;"
    return makeListFromRequest(cur,req,'period')

