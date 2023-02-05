import json

file  = "./checker.json"

def oneTimeEntry():
    with open(file,'r') as jfile:
        data = json.load(jfile)

    data['dbcheck'] = 1

    with open(file,'w') as jfile:
        json.dump(data,jfile)

def oneTimeCheck():
    with open(file,'r') as jfile:
        data = json.load(jfile)

    if(data["dbcheck"]== 1):
        return True        
    else:
        return False

if __name__ == "__main__":
    print("JSON CONTROLLER")