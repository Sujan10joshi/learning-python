string = "He is a good boy and he is a good player."
print(string.replace(" " , "_"))
print(string.replace("is" , "was"))
print(string.replace("is" , "was", 1))

is_pos1=string.find("is", 1)
is_pos2=string.find("is", is_pos1+1)
print(is_pos2)