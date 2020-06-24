def all_para(first_name, *args, last_name = 'unknown', **kwargs):
    print(first_name)
    print(args)
    print(last_name)
    print(kwargs)

all_para('sujan', 3,5,6, age=22, fav=10)