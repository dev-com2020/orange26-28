import csv

filename = "records.csv"

fields = []
rows = []

with open(filename, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Suma wierszy:", csvreader.line_num)

print(fields)
print(rows)
