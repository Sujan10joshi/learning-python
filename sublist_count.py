def sublist_count(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

nums = [1,2,3,[1,3,5,6,],[3,4,5,6],[5,8,3]]
print(sublist_count(nums))

