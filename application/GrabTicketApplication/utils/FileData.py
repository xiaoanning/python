#coding=utf-8

import json

def writeFile(filePath , data):
    
    with open(filePath , "w") as f :

        jsonData = json.dumps(data)
        json.dump(jsonData , f)

def readFile(filePath):
    
    with open(filePath , "r") as f:
        
        jsonData = json.load(f)
        jsonList = json.loads(jsonData)

        return jsonList 

def appendWriteFile(appendContent,filePath):
    with file(filePath,'r+') as file_obj :
        file_obj.read()
        file_obj.write("\n{}".format(appendContent))
        file_obj.close()
