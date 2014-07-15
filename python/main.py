import fileIO
import match


config = fileIO.openConfigFile()
licenseAttributes = fileIO.openJSONFile(config['config']['base'] + config['config']['attributes_files'])

print(licenseAttributes)

for license in licenseAttributes["licenses"]:
	licenseFile = license['trainingFile'];
	licensePath = config['training_folder'] + licenseFile
# print(config['config']['projects']);
