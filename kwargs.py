def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")


#func(name = 'sujan', age = 23)

d = {'first_name':'sujan', 'last_name':'joshi','age':22}
func(**d)   #dict unpacking