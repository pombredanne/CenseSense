import os

def openFile(file_path):
	f = open(file_location, 'r+')
	contents = f.read()
	return contents;

def openJSONFile(file_path):
	json_contents = openFile(openFile)
	data = json.load(json_contents)
	return data

def openConfigFile():
	return openJSONFile("../config.json")	

def openConfigFile():
	return openJSONFile("config.json")


def recursivelyReturnAllFiles(path):
	file_set = set()
	for dir_, _, files in os.walk(path):
	    for fileName in files:
	        relDir = os.path.relpath(dir_, path)
	        relFile = os.path.join(relDir, fileName)
	        file_set.add(relFile)
	return file_set;

def trainingFilesToArray(training_path):
	return recursivelyReturnAllFiles(training_path)

def getProjectFiles(project_path):
	return recursivelyReturnAllFiles(project_path)


print(trainingFilesToArray("../training/licenseContents/"));
print(getProjectFiles("../training/licenseContents/"))