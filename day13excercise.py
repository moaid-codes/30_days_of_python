"""
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filter_ = [i for i in numbers if i < 1]
print(filter_)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lst = [i for b in list_of_lists for i in b]
print(lst)

a = [(n, *(n**i for i in range(6))) for n in range(11)]
print(a)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
c =  [(f"{i[0]}".upper(),f"{i[0][:3]}".upper(), f"{i[1]}".upper()) for u in countries for i in u]
print(c)

b = [[{'country': f"{i[0]}".upper(), 'city':f"{i[1]}".upper()}] for u in countries for i in u]
print(b)
"""
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
ls = [(f"{i[0]}" + ' ' + f"{i[1]}") for u in names for i in u]
print(ls)
