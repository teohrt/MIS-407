import csv
from collections import defaultdict

fileName = "Iowa_Liquor_Sales-2017-partial.csv"

total = 0
table = defaultdict(lambda: 0)

# Store individual values for countys in a dictionary
with open(fileName) as csv_file :
    reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in reader :
        if line_count != 0:
            # County is the dictionary key, liters is the value being added
            k = row[8]
            if k != "" :
                table[k.title()] += float(row[22])
            total += float(row[22])
        line_count += 1

print("Alcohol sales by county:")
count = 1
for k, v in sorted(table.items()) :
    print("{0:3}. {1:15} {2:>10} liters".format(count, k, round(v, 2)))
    count += 1
print(f"Total: {round(total, 2)} liters")