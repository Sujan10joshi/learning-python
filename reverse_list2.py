elements = ['olleh', 'rm', 'najus', 'ris']

def reverse_list(r):
    rev = []
    for i in r:
        rev.append(i[::-1])
    return rev

print(elements)
print(reverse_list(elements))
