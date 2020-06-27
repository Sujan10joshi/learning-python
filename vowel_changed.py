def translate(word):
    new_word = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            new_word += "X"
        else:
            new_word += letter
    return new_word

print(translate(input("Enter any word: ")))