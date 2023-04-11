import csv
from typing import List, Union

def generateCsvFile(oldCsvFilePath: str, deleteAllExceptCols: List[int], newCsvFilePath: str, sep=',', colDeleteIndex: Union[int, None] = None, rowTobeDeleteDesreption: Union[str, None] = None, deleteHead: bool = False):
    
    # Create a set of column indices to be deleted
    colsTobeDeleted = set(range(len(next(csv.reader(open(oldCsvFilePath)))))) - set(deleteAllExceptCols)
    
    with open(oldCsvFilePath, 'r') as oldFile, open(newCsvFilePath, 'w', newline='') as newFile:
        reader = csv.reader(oldFile, delimiter=sep)
        writer = csv.writer(newFile, delimiter=sep)
        
        # Handle header
        if deleteHead:
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

# For Region Table 
generateCsvFile('./csv/original/region.csv',[0,5],'./csv/fill/fill_region.csv',deleteHead=True)

# # For Departement table
# generateCsvFile('./csv/original/departement.csv',[3,4,5],'./csv/fill/fill_departement.csv',deleteHead=True)

# # For commune table
# generateCsvFile('./csv/original/region.csv',[2,3,4,5],'./csv/fill/fill_region1.csv',deleteHead=True)

# # For Departement chefLieu table
# generateCsvFile('./csv/original/region.csv',[2,3,4,5],'./csv/fill/fill_region1.csv',deleteHead=True)

# # For RegionChefLieu chefLieu table
# generateCsvFile('./csv/original/region.csv',[2,3,4,5],'./csv/fill/fill_region1.csv',deleteHead=True)