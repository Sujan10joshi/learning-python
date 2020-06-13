#def is_palindrome(a,b):
#    if a == b:
#        return True
#    return False

#a = input("Enter any name: ")
#b = a[::-1]

#palindrome = is_palindrome(a,b)
#print(palindrome)


def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

word = input("Enter any name: ")
print(is_palindrome(word))