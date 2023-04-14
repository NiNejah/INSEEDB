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


def addColumn(csvFile: str, headers: List[str], intoIndex: List[int], values: List[str], sep: str):
    # Open the CSV file and create a list of rows
    with open(csvFile, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=sep)
        rows = list(reader)
    
    # Insert the new columns at the specified indices
    for header, index, value in zip(headers, intoIndex, values):
        for row in rows:
            row.insert(index, value)
        rows[0][index] = header  # Set the header of the new column at the correct position
            
    # Write the updated rows to the CSV file
    with open(csvFile, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=sep)
        for row in rows:
            writer.writerow(row)
# # # For Region Table
# generateCsvFile('./csv/original/region.csv',[0,5],'./csv/fill/fill_region.csv',deleteHeader=True)

# # # For Departement table
# generateCsvFile('./csv/original/departement.csv',[0,1,6],'./csv/fill/fill_departement.csv',deleteHeader=True)

# # # For commune table
# generateCsvFile('./csv/original/commune.csv',[1,3,9],'./csv/fill/fill_commune.csv',colDeleteIndex=0,rowTobeDeleteDesreption="COMD",deleteHeader=True)

# # # For Departement chefLieu table
# generateCsvFile('./csv/original/commune.csv',[1,3],'./csv/fill/fill_departement_chefLieu.csv',colDeleteIndex=0,rowTobeDeleteDesreption="COMD",deleteHeader=True)

# # # For RegionChefLieu chefLieu table
# generateCsvFile('./csv/original/commune.csv',[1,2],'./csv/fill/fill_region_chefLieu.csv',colDeleteIndex=0,rowTobeDeleteDesreption="COMD",deleteHeader=True)


# # # Population :
# # For Population 19
# generateCsvFile('./csv/vrg/dossier_complet.csv',[0,1],'./csv/fill/Population_19.csv',sep=';')
# addColumn('./csv/fill/Population_19.csv',['indicator','category','startyear','endyear'],[1,2,3,4],["pupulation","tous","2019",""],';')

# # For Population 19 H
# generateCsvFile('./csv/vrg/dossier_complet.csv',[0,toindex('J')],'./csv/fill/Population_19_H.csv',sep=';')

# # For Population 19 F
# generateCsvFile('./csv/vrg/dossier_complet.csv',[0,toindex('U')],'./csv/fill/Population_19_F.csv',sep=';')

# # For Population 19 0 - 14 tous :
# generateCsvFile('./csv/vrg/dossier_complet.csv',[0,2],'./csv/fill/Population_19_0014.csv',sep=';')


# # For Population 13
# generateCsvFile('./csv/vrg/dossier_complet.csv',[0,toindex('DB')],'./csv/fill/Population_13.csv',sep=';')

# # For Population 08
# generateCsvFile('./csv/vrg/dossier_complet.csv',[0,209],'./csv/fill/Population_08.csv',sep=';')
# addColumn('./csv/fill/Population_08.csv',["indicat","cat"],[1,3],["pupulation","2008"],';')

# # # TESTS : 
