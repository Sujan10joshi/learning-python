def  def_para(fname = 'unknown', lname = 'unknown', age = 'none'):
    print(f"your first name is {fname}.")
    print(f"your last name is {lname}.")
    print(f"your age is {age}.")

def_para()

#variable scope
x = 5
def scope():
    global x #global variable
    x = 9 #local variable
    return x

print(scope())
print(x)
