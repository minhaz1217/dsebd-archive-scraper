
from file_writer.csv_writer import writeCSV

def writeFile(data: list, path: str, type: int = 1):
    # type : 1 = csv, 2 = json
    if(type == 1):
        writeCSV(data, path)
    elif(type == 2):
        print("JSON")