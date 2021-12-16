# import csv & json packages 
import csv
import json

# create file path to CSV file
csvFilePath = 'apple_concepts_reduced.csv'


# create JSON file path
jsonFilePath = 'json_apple_concepts.json'


# create an empty list to store data
my_list = []


# open & read the CSV
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:
        name = row["TITLE"] # title?
        children = row["KEYWORDS"]
        my_dict = {"name":name, "children":children}
        my_list.append(my_dict)


with open(jsonFilePath, 'w') as outfile:
    json.dump(my_list, outfile, indent=4)


# with open(jsonFilePath, 'w') as jsonFile:
#     # make it more readable
#     jsonFile.write(json.dumps(data, indent=4))