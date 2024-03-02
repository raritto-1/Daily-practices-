import csv

file = 'name.csv'

with open(file,'r') as files:
    csv_reader= csv.reader(files)

    header = next(csv_reader)
    print('header',header)

    for row in csv_reader:
        print(row)
