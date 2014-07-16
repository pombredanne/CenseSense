import os
import json

def writeFile(file_path, contents):
	f = open(file_path, 'r+', encoding='utf-8')
	f.write(contents)

def openFile(file_path):
	return open(file_path, 'r', encoding='utf-8')

def openJSONFile(file_path):
	contents = openFile(file_path)
	data = json.load(contents)
	return data

def openConfigFile():
	return openJSONFile("../config.json")	

def recursivelyReturnAllFiles(path):
	file_set = set()
	for dir_, _, files in os.walk(path):
	    for fileName in files:
	        relDir = os.path.relpath(dir_, path)
	        relFile = os.path.join(relDir, fileName)
	        file_set.add(relFile)
	return file_set;

def getProjectFiles(project_path):
	return recursivelyReturnAllFiles(project_path)

def writeArrayAsJSONFile(file_path, objectArray):
	jsonString = json.dumps(objectArray, sort_keys=True, indent=4, separators=(',', ': '))
	writeFile(file_path, jsonString)