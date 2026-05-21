
'''
user_input = input("what is your age?")
age = int(user_input)
if age > 18:
    print("you are old enough to drive")
else:
    needed_years = 18 - age
    print("Wait ",needed_years, 'years to drive!')

bros_age = 30
if bros_age > age:
   difference =  bros_age - age
   print("you are ", difference, "years younger than unc")
else:
    difference = age - bros_age
    print("you are ", difference, "years older than unc")
    '''
'''
month = input("what is the month?")
if month in ('September', 'October', 'November'):
    print("It is Autumn!")
elif month in ('December', 'January', 'February'):
    print("It is Winter!")
elif month in ('March', 'April', 'May'):
    print("It is Spring!")
elif month in ('june', 'july', 'August'):
    print("It is Summer!")

'''

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    print(person['skills'][2])
else:
    print("the skills key doesn't exist")

if 'Python' in person['skills']:
    print("That person has mastered Python")
else:
    print("He don't got Python like that")
