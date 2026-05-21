

                                    #   DICTIONARIES

empty_dic = {}
example = {'key1':'value1', 'key2':'value2'}

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['age'])
print(person.get('test'))
person['job tittle'] = 'teacher'
print(person['job tittle'])
person['skills'].append('CSS')
print(person['skills'][5])

# Modyiiying the value of a key
person['is_marred'] = 'YES'
print(person['is_marred'])

del person['country']
print(person.get('country'))

person.pop('age')
print(person)

backup = person.items()
print(backup)

actual_backup = dict(person)
actual_backup.clear()
print(":3")
print(actual_backup)

del actual_backup

copy = person.copy()
print(len(copy))

keys = person.keys()
print(type(keys))

values = person.values()
print(type(values))
