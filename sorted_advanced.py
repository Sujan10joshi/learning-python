fruits = ['mango','orange','apple']
# fruits.sort()
# print(fruits)

fruits2 = ('mango','orange','apple')
# print(sorted(fruits))

fruits3 = {'mango','orange','apple'}
# print(sorted(fruits3))

bikes = [
    {'name' : 'duke 200', 'price' : 545000},
    {'name' : 'bullet 350', 'price' : 615000},
    {'name' : 'splender 150', 'price' : 205000},
    {'name' : 'benille 250', 'price' : 350000}
]
print(sorted(bikes, key = lambda d : d['price'], reverse=True))

    

