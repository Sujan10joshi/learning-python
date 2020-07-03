from csv import writer

with open('file1.csv', 'w', newline='') as f:
    write_csv =writer(f)
    # write_csv.writerow(['name', 'country'])
    # write_csv.writerow(['Sujan', 'Nepal'])
    # write_csv.writerow(['Kroos', 'Germany'])
    write_csv.writerows([['name', 'country'],['Sujan', 'Nepal'],['Kroos', 'Germany']])