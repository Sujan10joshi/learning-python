nums = (1,2,3,4.0)   #looping in tuples
for i in nums:
    print(i)
print(min(nums))
print(max(nums))
print(sum(nums))



#n = (1)   #tuple with one element
#num = (1,)
#word = ('word1',)

#print(type(n))
#print(type(num))
#print(type(word))


#bikes = 'pulsar', 'duke', 'fz', 'bullet'   #tuple without parenthesis
#print(type(bikes))

#riders = 'sujan joshi', 'prabin tiwari', 'sanjeet shrestha'    #tuple unpacking
#rider1, rider2, rider3 = (riders)
#print(rider1)
#print(rider3)

fruits = ('apple', ['mango', 'orange'])
fruits[1].pop()
fruits[1].append("grapes")
print(fruits)