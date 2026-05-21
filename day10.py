
                                        #               LOOPS



# WHILE

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 2:
        count = count + 1
        continue
    if count == 4:
        break

else:
    print(count)

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

language = 'Python'
for letter in language:
    print(letter)

idk = ['cats', 'dogs', 'horses', 'idk']
for something in idk:
    print(something)

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
for anythin, anything_2 in person.items():
    print(anythin, anything_2)

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    print(key)
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
else:
    print("The loop has ended")
