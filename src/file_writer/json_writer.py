import json

def write(datas : list, path: str):
    if(len(datas) == 0):
        raise ValueError("No data to write.")
        
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(datas, f, ensure_ascii=False, indent=4)
    print("JSON file created in ", path)
