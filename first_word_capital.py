def first_capi(l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

name = ['sujan', 'joshi']
#print(first_capi(name))
print(first_capi(name, reverse_str=True))