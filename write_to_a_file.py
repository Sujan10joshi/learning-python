# with open('file.txt', 'w') as f:      # w overwrites exiting text and writes new, can make new file simply
#     f.write('Hello there\n call me')

# with open('file2.txt', 'a') as f:      # a appends texts in exiting files and also can create a new file 
#     f.write('\nSo thi is appending exiting text')

with open('file3.txt', 'r+') as f:
    f.seek(len(f.read()))
    f.write('Please suscribe')