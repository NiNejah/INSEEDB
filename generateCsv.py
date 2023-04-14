import csv
from typing import List, Union
def toindex(col_header):
    """
    Converts a string column header into its corresponding index number.
    """
    col_header = col_header.upper()  # Convert to uppercase
    index = 0
    for i, char in enumerate(reversed(col_header)):
        index += (ord(char) - 64) * (26 ** i)
    return index - 1


def generateCsvFile(oldCsvFilePath: str, deleteAllExceptCols: List[int], newCsvFilePath: str, sep=',', colDeleteIndex: Union[int, None] = None, rowTobeDeleteDesreption: Union[str, None] = None, deleteHeader: bool = False):
    
    # Create a set of column indices to be deleted
    colsTobeDeleted = set(range(len(next(csv.reader(open(oldCsvFilePath)))))) - set(deleteAllExceptCols)
    
    with open(oldCsvFilePath, 'r') as oldFile, open(newCsvFilePath, 'w', newline='') as newFile:
        reader = csv.reader(oldFile, delimiter=sep)
        writer = csv.writer(newFile, delimiter=sep)
        
        # Handle header
        if deleteHeader:
            next(reader)  # Skip reading the first line (header) from the old CSV file
            # writer.writerow(deleteAllExceptCols)  # Write the new header to the new CSV file
        else:
            header = next(reader)
            writer.writerow([header[i] for i in deleteAllExceptCols])
        
        # Handle rows
        for row in reader:
            if colDeleteIndex is not None and row[colDeleteIndex] == rowTobeDeleteDesreption:
                continue
            
            writer.writerow([row[i] for i in deleteAllExceptCols if i not in colsTobeDeleted])

# # For Region Table 
# generateCsvFile('./csv/original/region.csv',[0,5],'./csv/fill/fill_region.csv',deleteHeader=True)

# # # For Departement table
# generateCsvFile('./csv/original/departement.csv',[0,1,6],'./csv/fill/fill_departement.csv',deleteHeader=True)

# # # For commune table
# generateCsvFile('./csv/original/commune.csv',[1,3,10],'./csv/fill/fill_commune.csv',colDeleteIndex=0,rowTobeDeleteDesreption="COMD",deleteHeader=True)

# # # For Departement chefLieu table
# generateCsvFile('./csv/original/commune.csv',[1,3],'./csv/fill/fill_departement_chefLieu.csv',colDeleteIndex=0,rowTobeDeleteDesreption="COMD",deleteHeader=True)

# # # For RegionChefLieu chefLieu table
# generateCsvFile('./csv/original/commune.csv',[1,2],'./csv/fill/fill_region_chefLieu.csv',colDeleteIndex=0,rowTobeDeleteDesreption="COMD",deleteHeader=True)



# Population : 
# # For Population 19 
# generateCsvFile('./csv/vrg/dossier_complet.csv',[0,1],'./csv/fill/Population_19.csv',sep=';')

# # For Population 19 H
# generateCsvFile('./csv/vrg/dossier_complet.csv',[0,toindex('J')],'./csv/fill/Population_19_H.csv',sep=';')

# # For Population 19 F
# generateCsvFile('./csv/vrg/dossier_complet.csv',[0,toindex('U')],'./csv/fill/Population_19_F.csv',sep=';')

# # For Population 13 
# generateCsvFile('./csv/vrg/dossier_complet.csv',[0,toindex('DB')],'./csv/fill/Population_13.csv',sep=';')

# # For Population 08 
# generateCsvFile('./csv/vrg/dossier_complet.csv',[0,toindex('HB')],'./csv/fill/Population_08.csv',sep=';')
