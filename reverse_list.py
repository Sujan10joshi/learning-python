numbers = [1,2,3,4]
words = ['word1', 'word2', 'word3']

#def reverse(n):
#    n.reverse()
#    return n

#def rev(l):
#    return l[::-1]
    
def reverse_list(s):
    rev = []
    for i in range(len(s)):
        popped_num = s.pop()
        rev.append(popped_num)
    return rev

print(reverse_list(numbers))