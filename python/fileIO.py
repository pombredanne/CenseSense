import os
import json

def openFile(file_path):
	return open(file_path, 'r')

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