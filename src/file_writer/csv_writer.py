import csv

def writeCSV(datas : list, path: str):
    if(len(datas) == 0):
        raise ValueError("No data to write.")

    a = datas[0]
    with open(path, 'a', newline="") as f:
        w = csv.DictWriter(f, a.keys())
        w.writeheader()
    
    for data in datas:
        with open(path, 'a', newline="") as f:
            w = csv.DictWriter(f, data.keys())
            w.writerow(data)
    
    print("CSV file created in ", path)