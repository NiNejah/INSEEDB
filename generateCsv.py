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

dataFile = './csv/vrg/dossier_complet.csv'
fillFile = './csv/fill/'

# # # Population :
#################################### 2019 ############################################
    # # For Population 2019 Tout:
# generateCsvFile(dataFile, [0,1], fillFile + 'Population_19.csv', sep=';')
# addColumn(fillFile + 'Population_19.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Population en 2019", "2019", ""], ';')

    # # For Population 2019 0 - 14 Tout :
# generateCsvFile(dataFile, [0,2], fillFile + 'Population_19_00_14.csv', sep=';')
# addColumn(fillFile + 'Population_19_00_14.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 0-14 ans en 2019", "2019", ""], ';')

    # # For Population 2019 15 - 29 Tout :
# generateCsvFile(dataFile, [0,3], fillFile + 'Population_19_15_29.csv', sep=';')
# addColumn(fillFile + 'Population_19_15_29.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 15-29 ans en 2019", "2019", ""], ';')

    # # For Population 2019 30 - 44 Tout :
# generateCsvFile(dataFile, [0,4], fillFile + 'Population_19_30_44.csv', sep=';')
# addColumn(fillFile + 'Population_19_30_44.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 30-44 ans en 2019", "2019", ""], ';')

    # # For Population 2019 45 - 59 Tout :
# generateCsvFile(dataFile, [0,5], fillFile + 'Population_19_45_59.csv', sep=';')
#addColumn(fillFile + 'Population_19_45_59.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 45-59 ans en 2019", "2019", ""], ';')

    # # For Population 2019 60 - 74 Tout :
# generateCsvFile(dataFile, [0,6], fillFile + 'Population_19_60_74.csv', sep=';')
# addColumn(fillFile + 'Population_19_60_74.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 60-74 ans en 2019", "2019", ""], ';')

    # # For Population 2019 75 - 89 Tout :
# generateCsvFile(dataFile, [0,7], fillFile + 'Population_19_75_89.csv', sep=';')
# addColumn(fillFile + 'Population_19_75_89.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 75-89 ans en 2019", "2019", ""], ';')

    # # For Population 2019 90 - Plus Tout :
# generateCsvFile(dataFile, [0,8], fillFile + 'Population_19_90_plus.csv', sep=';')
# addColumn(fillFile + 'Population_19_90_plus.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 90 ans ou plus en 2019", "2019", ""], ';')


######################################## Homme en 2019 #################################
    # # For Population 2019 Homme:
# generateCsvFile(dataFile ,[0,9], fillFile + 'Population_19_H.csv', sep=';')
# addColumn(fillFile + 'Population_19_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes en 2019", "2019", ""], ';')

    # # For Population 19 0 - 14 Homme :
# generateCsvFile(dataFile, [0,10], fillFile + 'Population_19_00_14_H.csv', sep=';')
# addColumn(fillFile + 'Population_19_00_14_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 0-14 ans en 2019", "2019", ""], ';')

    # # For Population 2019 15 - 29 Homme :
# generateCsvFile(dataFile, [0,11], fillFile + 'Population_19_15_29_H.csv', sep=';')
# addColumn(fillFile + 'Population_19_15_29_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 15-29 ans en 2019", "2019", ""], ';')

    # # For Population 2019 30 - 44 Homme :
# generateCsvFile(dataFile, [0,12], fillFile + 'Population_19_30_44_H.csv', sep=';')
# addColumn(fillFile + 'Population_19_30_44_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 30-44 ans en 2019", "2019", ""], ';')

    # # For Population 2019 45 - 59 Homme :
# generateCsvFile(dataFile, [0,13], fillFile + 'Population_19_45_59_H.csv', sep=';')
# addColumn(fillFile + 'Population_19_45_59_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 45-59 ans en 2019", "2019", ""], ';')

    # # For Population 2019 60 - 74 Homme :
# generateCsvFile(dataFile, [0,14], fillFile + 'Population_19_60_74_H.csv', sep=';')
# addColumn(fillFile + 'Population_19_60_74_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 60-74 ans en 2019", "2019", ""], ';')

    # # For Population 2019 75 - 89 Homme :
# generateCsvFile(dataFile, [0,15], fillFile + 'Population_19_75_89_H.csv', sep=';')
# addColumn(fillFile + 'Population_19_75_89_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 75-89 ans en 2019", "2019", ""], ';')

    # # For Population 2019 90 - Plus Homme :
# generateCsvFile(dataFile, [0,16], fillFile + 'Population_19_90_plus_H.csv', sep=';')
# addColumn(fillFile + 'Population_19_90_plus_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 90 ans ou plus en 2019", "2019", ""], ';')

######################################## Femme en 2019 #################################
# # For Population 2019 Femme:
# generateCsvFile(dataFile, [0,20], fillFile + 'Population_19_F.csv', sep=';')
# addColumn(fillFile + 'Population_19_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes en 2019", "2019", ""], ';')

    # # For Population 2019 0 - 14 Femme :
# generateCsvFile(dataFile, [0,21], fillFile + 'Population_19_00_14_F.csv', sep=';')
# addColumn(fillFile + 'Population_19_00_14_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 0-14 ans en 2019", "2019", ""], ';')

    # # For Population 2019 15 - 29 Femme :
# generateCsvFile(dataFile, [0,22], fillFile + 'Population_19_15_29_F.csv', sep=';')
# addColumn(fillFile + 'Population_19_15_29_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 15-29 ans en 2019", "2019", ""], ';')

    # # For Population 2019 30 - 44 Femme :
# generateCsvFile(dataFile, [0,23], fillFile + 'Population_19_30_44_F.csv', sep=';')
# addColumn(fillFile + 'Population_19_30_44_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 30-44 ans en 2019", "2019", ""], ';')

    # # For Population 2019 45 - 59 Femme :
# generateCsvFile(dataFile, [0,24], fillFile + 'Population_19_45_59_F.csv', sep=';')
# addColumn(fillFile + 'Population_19_45_59_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 45-59 ans en 2019", "2019", ""], ';')

    # # For Population 2019 60 - 74 Femme :
# generateCsvFile(dataFile, [0,25], fillFile + 'Population_19_60_74_F.csv', sep=';')
# addColumn(fillFile + 'Population_19_60_74_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 60-74 ans en 2019", "2019", ""], ';')

    # # For Population 2019 75 - 89 Femme :
# generateCsvFile(dataFile, [0,26], fillFile + 'Population_19_75_89_F.csv', sep=';')
# addColumn(fillFile + 'Population_19_75_89_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 75-89 ans en 2019", "2019", ""], ';')

    # # For Population 2019 90 - Plus Femme :
# generateCsvFile(dataFile, [0,27], fillFile + 'Population_19_90_plus_F.csv', sep=';')
# addColumn(fillFile + 'Population_19_90_plus_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 90 ans ou plus en 2019", "2019", ""], ';')

#################################### 2013 ############################################
# # For Population 2013 Tout:
# generateCsvFile(dataFile, [0,105], fillFile + 'Population_13.csv', sep=';')
# addColumn(fillFile + 'Population_13.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Population en 2013", "2013", ""], ';')

    # # For Population 2013 0 - 14 Tout :
# generateCsvFile(dataFile, [0,106], fillFile + 'Population_13_00_14.csv', sep=';')
# addColumn(fillFile + 'Population_13_00_14.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 0-14 ans en 2013", "2013", ""], ';')

    # # For Population 2013 15 - 29 Tout :
# generateCsvFile(dataFile, [0,107], fillFile + 'Population_13_15_29.csv', sep=';')
# addColumn(fillFile + 'Population_13_15_29.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 15-29 ans en 2013", "2013", ""], ';')

    # # For Population 2013 30 - 44 Tout :
# generateCsvFile(dataFile, [0,108], fillFile + 'Population_13_30_44.csv', sep=';')
# addColumn(fillFile + 'Population_13_30_44.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 30-44 ans en 2013", "2013", ""], ';')

    # # For Population 2013 45 - 59 Tout :
# generateCsvFile(dataFile, [0,109], fillFile + 'Population_13_45_59.csv', sep=';')
# addColumn(fillFile + 'Population_13_45_59.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 45-59 ans en 2013", "2013", ""], ';')

    # # For Population 2013 60 - 74 Tout :
# generateCsvFile(dataFile, [0,110], fillFile + 'Population_13_60_74.csv', sep=';')
# addColumn(fillFile + 'Population_13_60_74.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 60-74 ans en 2013", "2013", ""], ';')

    # # For Population 2013 75 - 89 Tout :
# generateCsvFile(dataFile, [0,111], fillFile + 'Population_13_75_89.csv', sep=';')
# addColumn(fillFile + 'Population_13_75_89.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 75-89 ans en 2013", "2013", ""], ';')

    # # For Population 2013 90 - Plus Tout :
# generateCsvFile(dataFile, [0,112], fillFile + 'Population_13_90_plus.csv', sep=';')
# addColumn(fillFile + 'Population_13_90_plus.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 90 ans ou plus en 2013", "2013", ""], ';')

######################################## Homme en 2013 #################################
    # # For Population 2013 Homme:
# generateCsvFile(dataFile, [0,113], fillFile + 'Population_13_H.csv', sep=';')
# addColumn(fillFile + 'Population_13_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes en 2013", "2013", ""], ';')

    # # For Population 2013 0 - 14 Homme :
# generateCsvFile(dataFile, [0,114], fillFile + 'Population_13_00_14_H.csv', sep=';')
# addColumn(fillFile + 'Population_13_00_14_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 0-14 ans en 2013", "2013", ""], ';')

    # # For Population 2013 15 - 29 Homme :
# generateCsvFile(dataFile, [0,115], fillFile + 'Population_13_15_29_H.csv', sep=';')
# addColumn(fillFile + 'Population_13_15_29_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 15-29 ans en 2013", "2013", ""], ';')

    # # For Population 2013 30 - 44 Homme :
# generateCsvFile(dataFile, [0,116], fillFile + 'Population_13_30_44_H.csv', sep=';')
# addColumn(fillFile + 'Population_13_30_44_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 30-44 ans en 2013", "2013", ""], ';')

    # # For Population 2013 45 - 59 Homme :
# generateCsvFile(dataFile, [0,117], fillFile + 'Population_13_45_59_H.csv', sep=';')
# addColumn(fillFile + 'Population_13_45_59_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 45-59 ans en 2013", "2013", ""], ';')

    # # For Population 2013 60 - 74 Homme :
# generateCsvFile(dataFile, [0,118], fillFile + 'Population_13_60_74_H.csv', sep=';')
# addColumn(fillFile + 'Population_13_60_74_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 60-74 ans en 2013", "2013", ""], ';')

    # # For Population 2013 75 - 89 Homme :
# generateCsvFile(dataFile, [0,119], fillFile + 'Population_13_75_89_H.csv', sep=';')
# addColumn(fillFile + 'Population_13_75_89_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 75-89 ans en 2013", "2013", ""], ';')

    # # For Population 2013 90 - Plus Homme :
# generateCsvFile(dataFile, [0,120], fillFile + 'Population_13_90_plus_H.csv', sep=';')
# addColumn(fillFile + 'Population_13_90_plus_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 90 ans ou plus en 2013", "2013", ""], ';')

######################################## Femme en 2013 #################################
    # # For Population 2013 Femme:
# generateCsvFile(dataFile, [0,124], fillFile + 'Population_13_F.csv', sep=';')
# addColumn(fillFile + 'Population_13_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes en 2013", "2013", ""], ';')

    # # For Population 2013 0 - 14 Femme :
# generateCsvFile(dataFile, [0,125], fillFile + 'Population_13_00_14_F.csv', sep=';')
# addColumn(fillFile + 'Population_13_00_14_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 0-14 ans en 2013", "2013", ""], ';')

    # # For Population 2013 15 - 29 Femme :
# generateCsvFile(dataFile, [0,126], fillFile + 'Population_13_15_29_F.csv', sep=';')
# addColumn(fillFile + 'Population_13_15_29_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 15-29 ans en 2013", "2013", ""], ';')

    # # For Population 2013 30 - 44 Femme :
# generateCsvFile(dataFile, [0,127], fillFile + 'Population_13_30_44_F.csv', sep=';')
# addColumn(fillFile + 'Population_13_30_44_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 30-44 ans en 2013", "2013", ""], ';')

    # # For Population 2013 45 - 59 Femme :
# generateCsvFile(dataFile, [0,128], fillFile + 'Population_13_45_59_F.csv', sep=';')
# addColumn(fillFile + 'Population_13_45_59_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 45-59 ans en 2013", "2013", ""], ';')

    # # For Population 2013 60 - 74 Femme :
# generateCsvFile(dataFile, [0,129], fillFile + 'Population_13_60_74_F.csv', sep=';')
# addColumn(fillFile + 'Population_13_60_74_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 60-74 ans en 2013", "2013", ""], ';')

    # # For Population 2013 75 - 89 Femme :
# generateCsvFile(dataFile, [0,130], fillFile + 'Population_13_75_89_F.csv', sep=';')
# addColumn(fillFile + 'Population_13_75_89_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 75-89 ans en 2013", "2013", ""], ';')

    # # For Population 2013 90 - Plus Femme :
# generateCsvFile(dataFile, [0,131], fillFile + 'Population_13_90_plus_F.csv', sep=';')
# addColumn(fillFile + 'Population_13_90_plus_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 90 ans ou plus en 2013", "2013", ""], ';')

#################################### 2008 ############################################
    # # For Population 2008 Tout:
# generateCsvFile(dataFile, [0,209], fillFile + 'Population_08.csv', sep=';')
# addColumn(fillFile + 'Population_08.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Population en 2008", "2008", ""], ';')

    # # For Population 2008 0 - 14 Tout :
# generateCsvFile(dataFile, [0,210], fillFile + 'Population_08_00_14.csv', sep=';')
# addColumn(fillFile + 'Population_08_00_14.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 0-14 ans en 2008", "2008", ""], ';')

    # # For Population 2008 15 - 29 Tout :
# generateCsvFile(dataFile, [0,211], fillFile + 'Population_08_15_29.csv', sep=';')
# addColumn(fillFile + 'Population_08_15_29.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 15-29 ans en 2008", "2008", ""], ';')

    # # For Population 2008 30 - 44 Tout :
# generateCsvFile(dataFile, [0,212], fillFile + 'Population_08_30_44.csv', sep=';')
# addColumn(fillFile + 'Population_08_30_44.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 30-44 ans en 2008", "2008", ""], ';')

    # # For Population 2008 45 - 59 Tout :
# generateCsvFile(dataFile, [0,213], fillFile + 'Population_08_45_59.csv', sep=';')
# addColumn(fillFile + 'Population_08_45_59.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 45-59 ans en 2008", "2008", ""], ';')

    # # For Population 2008 60 - 74 Tout :
# generateCsvFile(dataFile, [0,214], fillFile + 'Population_08_60_74.csv', sep=';')
# addColumn(fillFile + 'Population_08_60_74.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 60-74 ans en 2008", "2008", ""], ';')

    # # For Population 2008 75 - plus Tout :
# generateCsvFile(dataFile, [0,215], fillFile + 'Population_08_75_plus.csv', sep=';')
# addColumn(fillFile + 'Population_08_75_plus.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop 75 ans ou plus en 2008", "2008", ""], ';')

    # # For Population 2008 90 - Plus Tout :

######################################## Homme en 2008 #################################
    # # For Population 2008 Homme:
# generateCsvFile(dataFile, [0,216], fillFile + 'Population_08_H.csv', sep=';')
# addColumn(fillFile + 'Population_08_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes en 2008", "2008", ""], ';')

    # # For Population 2008 0 - 14 Homme :
# generateCsvFile(dataFile, [0,217], fillFile + 'Population_08_00_14_H.csv', sep=';')
# addColumn(fillFile + 'Population_08_00_14_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 0-14 ans en 2008", "2008", ""], ';')

    # # For Population 2008 15 - 29 Homme :
# generateCsvFile(dataFile, [0,218], fillFile + 'Population_08_15_29_H.csv', sep=';')
# addColumn(fillFile + 'Population_08_15_29_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 15-29 ans en 2008", "2008", ""], ';')

    # # For Population 2008 30 - 44 Homme :
# generateCsvFile(dataFile, [0,219], fillFile + 'Population_08_30_44_H.csv', sep=';')
# addColumn(fillFile + 'Population_08_30_44_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 30-44 ans en 2008", "2008", ""], ';')

    # # For Population 2008 45 - 59 Homme :
# generateCsvFile(dataFile, [0,220], fillFile + 'Population_08_45_59_H.csv', sep=';')
# addColumn(fillFile + 'Population_08_45_59_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 45-59 ans en 2008", "2008", ""], ';')

    # # For Population 2008 60 - 74 Homme :
# generateCsvFile(dataFile, [0,221], fillFile + 'Population_08_60_74_H.csv', sep=';')
# addColumn(fillFile + 'Population_08_60_74_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 60-74 ans en 2008", "2008", ""], ';')

    # # For Population 2008 75 - 89 Homme :
# generateCsvFile(dataFile, [0,222], fillFile + 'Population_08_75_89_H.csv', sep=';')
# addColumn(fillFile + 'Population_08_75_89_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 75-89 ans en 2008", "2008", ""], ';')

    # # For Population 2008 90 - Plus Homme :
# generateCsvFile(dataFile, [0,223], fillFile + 'Population_08_90_plus_H.csv', sep=';')
# addColumn(fillFile + 'Population_08_90_plus_H.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Hommes 90 ans ou plus en 2008", "2008", ""], ';')

######################################## Femme en 2008 #################################
    # # For Population 2008 Femme:
# generateCsvFile(dataFile, [0,227], fillFile + 'Population_08_F.csv', sep=';')
# addColumn(fillFile + 'Population_08_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes en 2008", "2008", ""], ';')

    # # For Population 2008 0 - 14 Femme :
# generateCsvFile(dataFile, [0,228], fillFile + 'Population_08_00_14_F.csv', sep=';')
# addColumn(fillFile + 'Population_08_00_14_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 0-14 ans en 2008", "2008", ""], ';')

    # # For Population 2008 15 - 29 Femme :
# generateCsvFile(dataFile, [0,229], fillFile + 'Population_08_15_29_F.csv', sep=';')
# addColumn(fillFile + 'Population_08_15_29_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 15-29 ans en 2008", "2008", ""], ';')

    # # For Population 2008 30 - 44 Femme :
# generateCsvFile(dataFile, [0,230], fillFile + 'Population_08_30_44_F.csv', sep=';')
# addColumn(fillFile + 'Population_08_30_44_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 30-44 ans en 2008", "2008", ""], ';')

    # # For Population 2008 45 - 59 Femme :
# generateCsvFile(dataFile, [0,231], fillFile + 'Population_08_45_59_F.csv', sep=';')
# addColumn(fillFile + 'Population_08_45_59_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 45-59 ans en 2008", "2008", ""], ';')

    # # For Population 2008 60 - 74 Femme :
# generateCsvFile(dataFile, [0,232], fillFile + 'Population_08_60_74_F.csv', sep=';')
# addColumn(fillFile + 'Population_08_60_74_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 60-74 ans en 2008", "2008", ""], ';')

    # # For Population 2008 75 - 89 Femme :
# generateCsvFile(dataFile, [0,233], fillFile + 'Population_08_75_89_F.csv', sep=';')
# addColumn(fillFile + 'Population_08_75_89_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 75-89 ans en 2008", "2008", ""], ';')

    # # For Population 2008 90 - Plus Femme :
# generateCsvFile(dataFile, [0,234], fillFile + 'Population_08_90_plus_F.csv', sep=';')
# addColumn(fillFile + 'Population_08_90_plus_F.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Population", "Pop Femmes 90 ans ou plus en 2008", "2008", ""], ';')

######################################## Naissances #################################
    # # # Naissance 2013 - 2019
# generateCsvFile(dataFile, [0,1501], fillFile + 'Naissances_13_19.csv', sep=';')
# addColumn(fillFile + 'Naissances_13_19.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances entre 2013 et 2019", "2013", "2019"], ';')

    # # # Naissance 2008 - 2013
# generateCsvFile(dataFile, [0,1502], fillFile + 'Naissances_08_13.csv', sep=';')
# addColumn(fillFile + 'Naissances_08_13.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances entre 2008 et 2013", "2008", "2013"], ';')

    # # # Naissance 1999 - 2008
# generateCsvFile(dataFile, [0,1503], fillFile + 'Naissances_99_08.csv', sep=';')
# addColumn(fillFile + 'Naissances_99_08.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances entre 1999 et 2008", "1999", "2008"], ';')

    # # # Naissance 1990 - 1999
# generateCsvFile(dataFile, [0,1504], fillFile + 'Naissances_90_99.csv', sep=';')
# addColumn(fillFile + 'Naissances_90_99.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances entre 1990 et 1999", "1990", "1999"], ';')

    # # # Naissance 1982 - 1990
# generateCsvFile(dataFile, [0,1505], fillFile + 'Naissances_82_90.csv', sep=';')
# addColumn(fillFile + 'Naissances_82_90.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances entre 1982 et 1990", "1982", "1990"], ';')

    # # # Naissance 1975 - 1982
# generateCsvFile(dataFile, [0,1506], fillFile + 'Naissances_75_82.csv', sep=';')
# addColumn(fillFile + 'Naissances_75_82.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances entre 1975 et 1982", "1975", "1982"], ';')

    # # # Naissance 1968 - 1975
# generateCsvFile(dataFile, [0,1507], fillFile + 'Naissances_68_75.csv', sep=';')
# addColumn(fillFile + 'Naissances_68_75.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances entre 1968 et 1975", "1968", "1975"], ';')

######################################## Naissances Domiciliées #################################
    # # # Naissance 2014
# generateCsvFile(dataFile, [0,1540], fillFile + 'Naissances_domiliees_14.csv', sep=';')
# addColumn(fillFile + 'Naissances_domiliees_14.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances domiciliées en 2014", "2014", ""], ';')

    # # # Naissance 2015
# generateCsvFile(dataFile, [0,1541], fillFile + 'Naissances_domiliees_15.csv', sep=';')
# addColumn(fillFile + 'Naissances_domiliees_15.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances domiciliées en 2015", "2015", ""], ';')

    # # # Naissance 2016
# generateCsvFile(dataFile, [0,1542], fillFile + 'Naissances_domiliees_16.csv', sep=';')
# addColumn(fillFile + 'Naissances_domiliees_16.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances domiciliées en 2016", "2016", ""], ';')

    # # # Naissance 2017
# generateCsvFile(dataFile, [0,1543], fillFile + 'Naissances_domiliees_17.csv', sep=';')
# addColumn(fillFile + 'Naissances_domiliees_17.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances domiciliées en 2017", "2017", ""], ';')

    # # # Naissance 2018
# generateCsvFile(dataFile, [0,1544], fillFile + 'Naissances_domiliees_18.csv', sep=';')
# addColumn(fillFile + 'Naissances_domiliees_18.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances domiciliées en 2018", "2018", ""], ';')

    # # # Naissance 2019
# generateCsvFile(dataFile, [0,1545], fillFile + 'Naissances_domiliees_19.csv', sep=';')
# addColumn(fillFile + 'Naissances_domiliees_19.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances domiciliées en 2019", "2019", ""], ';')

    # # # Naissance 2020
# generateCsvFile(dataFile, [0,1546], fillFile + 'Naissances_domiliees_20.csv', sep=';')
# addColumn(fillFile + 'Naissances_domiliees_20.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances domiciliées en 2020", "2020", ""], ';')

    # # # Naissance 2021
# generateCsvFile(dataFile, [0,1547], fillFile + 'Naissances_domiliees_21.csv', sep=';')
# addColumn(fillFile + 'Naissances_domiliees_21.csv', ['indicator', 'category', 'startyear', 'endyear'], [1,2,3,4], ["Naissances", "Naissances domiciliées en 2021", "2021", ""], ';')

## ...................

# # # TESTS : 
