import csv
filename = "C:/Users/nithy/Downloads/aapl.csv"  # corrected path
rows = []
fields = []

# Open the CSV file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Extract the header fields
    fields = next(csvreader)

    # Extract the remaining data rows
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d" % csvreader.line_num)
    print('Field names are: ' + ', '.join(field for field in fields))

    print('\nFirst 5 rows are:\n')
    for row in rows[:5]:
        for col in row:
            print("%10s" % col, end=" ")
        print('\n')

#adding details
import csv 
fields = ['Name', 'Branch', 'Year', 'CGPA'] 
rows = [ ['Nikhil', 'COE', '2', '9.0'], 
['Sanchit', 'COE', '2', '9.1'], 
['Aditya', 'IT', '2', '9.3'], 
['Sagar', 'SE', '1', '9.5'], 
['Prateek', 'MCE', '3', '7.8'], 
['Sahil', 'EP', '2', '9.1']] 
filename = "university_records.csv"
with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(rows)

