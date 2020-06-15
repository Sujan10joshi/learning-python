def common_betn_two(l,s):
    common = []
    for i in l:
        if i in s:
            common.append(i)
    return common

print(common_betn_two([1,3,5,6,8], [1,2,3,5,7,8,0]))


