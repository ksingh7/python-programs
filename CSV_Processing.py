import csv

# Write to CSV file

file = open('/Users/ksingh/temp/remove.csv','a')
csv_writer = csv.writer(file)
csv_writer.writerow(['Today','Maggie','coffee'])
file.close()

# Read the CSV file

file = open('/Users/ksingh/temp/remove.csv')
csv_reader = csv.reader(file)
for row in csv_reader:
    print row
    #print row[2]
file.close()

