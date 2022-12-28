
from file_writer.csv_writer import write as csvWriter
from file_writer.json_writer import write as jsonWriter

def writeFile(data: list, path: str, type: int = 1):
    # type : 1 = csv, 2 = json
    if(type == 1):
        csvWriter(data, path)
    elif(type == 2):
        jsonWriter(data, path)
    else:
        raise ValueError("type needs to be either 1 or 2")