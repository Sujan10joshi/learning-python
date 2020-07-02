f = open(r'D:\python\practice\text files\text.txt')

# print(f"cursar point - {f.tell()}")
# print(f.read())

# print(f"cursar point - {f.tell()}")
# print(f.read())

# print('before seek method\n')
# print("after seek method")
# print(f.seek(0))
# print(f.read())

# print(f.readline(), end='')
# print(f.readline())
# print(f.readline(), end='')

# lines = f.readlines()
# # print(len(lines))
# for line in lines:
#     print(line, end='')

# print(f.name)
# print(f.closed)

for line in f.readlines()[:2]:
    print(line, end='')

f.close()