with open('file.txt', 'r') as rf:
    with open('file3.txt', 'r+') as wf:
        for line in rf.readlines():
            name, salary = line.split(",")
            wf.write(f"{name}\'s salary is {salary}")