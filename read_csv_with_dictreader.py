from csv import DictReader

with open('first_csv.csv', 'r') as f:
    csv_reader = DictReader(f, delimiter = '|')
    for row in csv_reader:
        print(row['email'])