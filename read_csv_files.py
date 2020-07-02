from csv import reader

with open('first_csv.csv', 'r') as f:
    data = reader(f)
    next(data)
    for row in data:
        print(row)