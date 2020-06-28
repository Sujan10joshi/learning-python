import time


square = (i**2 for i in range (1, 11))
for num in square:
    print(num)
            #doesn't print two times because it is iterator and returns one num from memory and removes
for num in square:
    print(num)


            # time taken to perform list vs generator
# t1 = time.time()
# l = [i**2 for i in range(1000000)]
# g = (i**2 for i in range(100000))
# print(time.time()- t1)