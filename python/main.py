import fileIO
import match
import hashlib


config = fileIO.openConfigFile()
config = config["config"];

preprocessedFileName = "preprocessed.json"

# JSON listing all the licenses supported, each of their comparable
# traits, and their 
licenseAttributes = fileIO.openJSONFile(config['base'] + config['attributes_files'])

print("Beginning to scan through project files defined in config.")
for project in config["projects"]:
	foundLicenses = []
	preprocessed = fileIO.openJSONFile(config["base"]+project["preprocessed"] + preprocessedFileName)
	filesToProcess = fileIO.getProjectFiles(config["base"]+project["location"])

	# Need to at some point remove the processing of the JSON file
	# that stores preproccessed files.

	print("Files indexed in "+project['name']+", attempting to match them against licenses.")

	for document in filesToProcess:
		if preprocessedFileName not in document:
			hashOfFile = hashlib.md5(fileIO.openFile(config['base']+project["location"]+document).read().encode('utf-8')).hexdigest()
			hashOfFile = str(hashOfFile);
			
			# A flag that signals a chance to the
			# preprocessed file of an individual project.
			editToPreprocessed = 0

			for license in licenseAttributes["licenses"]:
				if(hashOfFile in preprocessed['preprocessed']):
					# In most cases I don't imagine a user is going to add their own
					# license file. However, if they want to, we still want to utilise
					# the preprocessed speedup.
					if(license in preprocessed['preprocessed'][hashOfFile]):
						if(preprocessed['preprocessed'][hashOfFile][license] == "true"):
							foundLicenses.append(license)

					# Else exists to handle the addition of a license,
					# after we've already preprocessed a file. 
					else:
						# We are going to have to modify the preprocessed file.
						editToPreprocessed = 1
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


						percentage = match.levenshteinPercentage(licenseData['license']['contents'], fileIO.openFile(config['base'] + project["location"]+document).read().encode('utf-8'))
						if(percentage > threshold):
							preprocessed['preprocessed'][hashOfFile][license] = "true"
						else:
							preprocessed['preprocessed'][hashOfFile][license] = "false"

					
				else:
					editToPreprocessed = 1
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

					# Compute the levenshtein difference.
					percentage = match.levenshteinPercentage(licenseData['license']['contents'], fileIO.openFile(config['base'] + project["location"]+document).read().encode('utf-8'))
					
					preprocessed['preprocessed'][hashOfFile] = {}
					
					# Now we do the actual comparison.
					print("Percentage : " + str(percentage))
					print("Threshold : " + str(threshold))
					if(percentage > threshold):
						preprocessed['preprocessed'][hashOfFile][license] = "true"
					else:
						preprocessed['preprocessed'][hashOfFile][license] = "false"

				

	if(editToPreprocessed):
		fileIO.writeArrayAsJSONFile(config["base"]+project["preprocessed"], preprocessed)

	print(foundLicenses)