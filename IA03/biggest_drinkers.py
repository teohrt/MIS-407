import csv
import operator
from collections import defaultdict

# salesFile = "Iowa_Liquor_Sales-2017-partial.csv"
# populationFile = "iowa_county_pop.csv"
# outputFilename = "output.txt"
salesFile = input("What is the county population filename?: ")
populationFile = input("What is the Iowa alcohol sales filename?: ")
outputFilename = input("What is the output filename?: ")
outputFile = open(outputFilename, "w")

salesTable = defaultdict(lambda: 0)
perCapitaTable = defaultdict(lambda: 0)

# Store individual volume values for counties in 'salesTable' dictionary
with open(salesFile) as csv_file :
    reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in reader :
        if line_count != 0:
            # County is the dictionary key, liters is the value being added
            k = row[8]
            if k != "" :
                salesTable[k.title()] += float(row[22])
        line_count += 1

# Store counties' volume per capita in 'perCapitaTable' dictionary
with open(populationFile) as csv_file :
    reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in reader :
        if line_count != 0:
            # County is the dictionary key, volume per capita is the value being added
            k = row[1].title()
            if k != "" :
                perCapitaTable[k] += float(salesTable[k] /float(row[2].replace(',', '')))
        line_count += 1

# Output the results
outputFile.write("Iowa counties' alcohol sale volume per capita:\n")
count = 1
for k, v in sorted(perCapitaTable.items(), key=operator.itemgetter(1), reverse=True) :
    outputFile.write("{0:3}. {1:15} {2:>10} liters per person\n".format(count, k, round(v, 2)))
    count += 1
outputFile.close()