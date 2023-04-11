import csv

def generateCsvFile(oldCsvFilePath, colsTobeDeleted, newCsvFilePath, sep=',', colDeleteIndex=None, rowTobeDeleteDesreption=None, deleteHead=False):
    # Open the old CSV file for reading
    with open(oldCsvFilePath, 'r') as oldCsvFile:
        # Open the new CSV file for writing
        with open(newCsvFilePath, 'w', newline='') as newCsvFile:
            # Create a CSV writer for the new file
            writer = csv.writer(newCsvFile, delimiter=sep)
            
            # Read the old CSV file using a CSV reader
            reader = csv.reader(oldCsvFile, delimiter=sep)
            
            # Find the index of the column to be deleted, if provided
            if colDeleteIndex is not None:
                colDeleteIndex = int(colDeleteIndex) - 1
            
            # Find the indices of the columns to be deleted in the new CSV file
            colsTobeDeleted = [int(i) - 1 for i in colsTobeDeleted]
            
            # Write the header row to the new CSV file, if not deleted
            if not deleteHead:
                header = next(reader)
                if colDeleteIndex is not None:
                    header = [header[i] for i in range(len(header)) if i != colDeleteIndex]
                newHeader = [header[i] for i in range(len(header)) if i not in colsTobeDeleted]
                writer.writerow(newHeader)
            else:
                # Skip the header row
                next(reader)
            # Write the remaining rows to the new CSV file
            for row in reader:
                if colDeleteIndex is not None and row[colDeleteIndex] == rowTobeDeleteDesreption:
                    continue
                newRow = [row[i] for i in range(len(row)) if i not in colsTobeDeleted]
                writer.writerow(newRow)



generateCsvFile('./csv/original/region.csv',[2,3,4,5],'./csv/new_fill_region1.csv',deleteHead=True)