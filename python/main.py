import fileIO
import match
import hashlib


config = fileIO.openConfigFile()
config = config["config"];

# JSON listing all the licenses supported, each of their comparable
# traits, and their 
licenseAttributes = fileIO.openJSONFile(config['base'] + config['attributes_files'])

print("Beginning to scan through project files defined in config.\n")
for project in config["projects"]:
	preprocessed = fileIO.openJSONFile(config["base"]+project["preprocessed"])
	filesToProcess = fileIO.getProjectFiles(config["base"]+project["location"])

	# Need to at some point remove the processing of the JSON file
	# that stores preproccessed files.
	for document in filesToProcess:
		hashOfFile = hashlib.md5(fileIO.openFile(config['base']+project["location"]+document).read().encode('utf-8')).hexdigest()
		hashOfFile = str(hashOfFile);

		print("Files indexed, attempting to match them against licenses.\n")
		for license in licenseAttributes["licenses"]:
			if(hashOfFile in preprocessed):
				print("nothing here")


			else:
				licenseFile = licenseAttributes["licenses"][license]["trainingFile"]
				licensePath = config['base'] + config['training_folder'] + licenseFile
				licenseData = fileIO.openJSONFile(licensePath)
				
				threshold = licenseAttributes["licenses"][license]["match_required"];

				# If the user for whatever reason decides to have different
				# types of percentages matched throughout files.
				# type cast to float because we are pulling strings out of a file
				# don't want to have inconsistencies in how it is handled.
				if(threshold == "default"):
					threshold =  float(config["default_match"])
				else:
					threshold = float(threshold)
				print(licenseData['license'][string])
				percentage = match.levenshteinPercentage(licenseData[license]['contents'], config['base']+fileIO.openFile(project["location"]+document).read().encode('utf-8'))
				if(percentage > threshold):
					preprocessed[hashOfFile][license] = "true"
				else:
					preprocessed[hashOfFile][license] = "false"

				

