import psycopg2
import psycopg2.extras 

DBNAME = "insee"
USERNAME="postgres"
PASS="1111"


# connect to an existing database
def connect(dbName , userName , Pass):
    print('Connexion à la base de données...')
    try:
        conn = psycopg2.connect("host=localhost dbname="+dbName+" user="+userName+" password="+Pass)
        return conn ; 
    except Exception as e :
        exit("Connexion impossible à la base de données: " + str(e)) 
    
def insertRegion(conn, cur, id, name):
    print ("Region insertion : ")
    try:
        cur.execute("""
        insert into Region( IdRegion , NomRegion ) 
        values (%s,%s);
        """,(id,name))
    except Exception as e :
        #fermeture de la connexion
        cur.close()
        conn.close()
        exit("error when try to insert Region : (id  = " + id + ", name = " + name) 

def insertDepartement(conn, cur, idD, name,idR):
    print ("Departement insertion : ")
    try:
        cur.execute("""
        insert into Departement (IdDepartement , NomDepartement , IdRegion )
        values (%s,%s,%s);
        """,(idD,name,idR))
    except Exception as e :
        #fermeture de la connexion
        cur.close()
        conn.close()
        exit("error when try to insert Departement : (idD  = " + idD + ", idR  ="  + idR + ", name = " + name)

def insertCommune(conn, cur, idC, name,idD):
    print ("Commune insertion : ")
    try:
        cur.execute("""
        insert into Commune (IdCommune, NomCommune, IdDepartement)
        values (%s,%s,%s);
        """,(idC,name,idD))
    except Exception as e :
        #fermeture de la connexion
        cur.close()
        conn.close()
        exit("error when try to insert Commune : (idC  = " + idC + ", idD  ="  + idD + ", name = " + name)


def insertDeptChefLieu(conn, cur, IdCommune, IdDepartement):
    print ("DeptChefLieu insertion : ")
    try:
        cur.execute("""
        insert into DeptChefLieu (IdCommune,IdDepartement) 
        values (%s,%s);
        """,(IdCommune,IdDepartement))
    except Exception as e :
        #fermeture de la connexion
        cur.close()
        conn.close()
        exit("error when try to insert DeptChefLieu : (IdCommune  = " + IdCommune + ", IdDepartement = " + IdDepartement) 

def insertRegionChefLieu(conn, cur, IdCommune, IdRegion):
    print ("RegionChefLieu insertion : ")
    try:
        cur.execute("""
        insert into RegionChefLieu (IdCommune, IdRegion) 
        values (%s,%s);
        """,(IdCommune,IdRegion))
    except Exception as e :
        #fermeture de la connexion
        cur.close()
        conn.close()
        exit("error when try to insert RegionChefLieu : (IdCommune  = " + IdCommune + ", IdRegion = " + IdRegion) 
    
def sqlRequest(conn, cur, cmd):
    print ("RegionChefLieu insertion : ")
    try:
        cur.execute("""
        %s
        """,(cmd))
    except Exception as e :
        #fermeture de la connexion
        cur.close()
        conn.close()
        exit("error when try to get : "+cmd) 
    
if __name__ == "__main__" : 
    print ("welcome to postState ...")
    conn = connect(DBNAME,USERNAME,PASS)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    

