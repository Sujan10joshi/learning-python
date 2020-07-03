from csv import DictWriter

with open('file2.csv', 'w', newline='') as f:
    csv_writer = DictWriter(f, fieldnames = ['firstname', 'lastname', 'age'])
    csv_writer.writeheader()
    # csv_writer.writerow({
    #     'firstname' : 'Sujan',
    #     'lastname' : 'Joshi',
    #     'age' : 22
    # })
    # csv_writer.writerow({
    #     'firstname' : 'David',
    #     'lastname' : 'Silva',
    #     'age' : 30
    # }
    # )

    csv_writer.writerows([
        {'firstname' : 'Sujan', 'lastname' : 'Joshi', 'age' : 22},
        {'firstname' : 'Leroy', 'lastname' : 'Sane', 'age' : 26},
        {'firstname' : 'Arjen', 'lastname' : 'Robben', 'age' : 34}
    ])