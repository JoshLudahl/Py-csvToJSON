# Purpose is to convert a csv file to a JSON file (.json)
# it takes 'input.csv' and outputs 'output.json'

import csv, os, json

# Take 'input.csv' 
csvFile = open('input.csv')

# Read the file
readObj = csv.reader(csvFile)

# Placeholder for the json objects
csvRows = []
titles = []

# Start iterating through the file, row by row
for row in readObj:
  if readObj.line_num == 1:
    for item in row:
      titles.append(item.strip())
  newObj = {}
  for i in range(len(row)):
      newObj[titles[i]] = row[i].strip()
  csvRows.append(newObj)

# Remove the first row   
csvRows.pop(0)

# Output to 'output.json'
newJSONObj = open('output.json', 'w')
jsonDump = json.dumps(csvRows)
newJSONObj.write(jsonDump)
newJSONObj.close()
