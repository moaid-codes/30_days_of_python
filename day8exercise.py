

dog = {}

print(type(dog))
dog['name'] = 'idk'
dog['color'] = 'black'
print(dog)

student = {'first name':'idk', 'last name':'idk', 'city':'LA', 'gender':'Dude', 'age':'38', 'marital status':'single as hell', 'address':'mars', 'skills':['Python', 'HTML', 'CSS']}
print(len(student))

print(student['skills'])
print(type(student['skills']))

student['skills'].append('break dancing')
print(student['skills'])

keys = student.keys()
print(keys)

values = student.values()
print(values)

dictionary_but_list = dict(student.items())
print(type(dictionary_but_list))
print(dictionary_but_list)

del student['age']
print(student)

del student
