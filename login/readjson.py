import json

def readjson():
    with open('data.json') as f:
        datalist = json.load(f)
        newlist = []
        for data in datalist:
            newlist.append(tuple(data.values()))
    return newlist