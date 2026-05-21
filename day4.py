


#STRINGS


# Escape sequences

'''
print("hello\nworld")  # \n starts a new line inn the middle of the string
print("hello\tworld")  # \t mimicks a tab before continuing the string
print("this is how you type a backslash \\")  # self explanatory
print("this is how you use double and single quotes \"\'") # i just spelled it out for you man
'''

# New Style string formattin

first_name = "lebron"
last_name = "james"
language = "Python"
formatted_string = "I am{} {}. I know Python btw".format(first_name,last_name, language)
print(formatted_string)
'''
a=4
b=3

print("{} + {} = {}".format(a,b, a+b))
print("{} / {} = {:.2f}".format(a,b, a/b)) # limits it to two digits after the decimel
'''
# String Interpolation. The current standard

a=4
b=3
print(f'{a} + {b} = {a+b}')
print(f'{a} / {b} = {a/b:.2f}')

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

print(language[-1], language[0])
print(language[0:3])
print(language[3:])
print(language[::-1])

# String Methods

challenge = 'thirty days of python'
print(challenge.capitalize()) # Capitalizes the string for you

print(challenge.count('y')) # counts the occurences of your argument
print(challenge.count('y', 7, 14)) # counts the occurences of your argument in a specific index range

print(challenge.endswith('on'))   # True # Checks if the string ends with your argument
print(challenge.endswith('tion')) # Falschallenge = 'thirty days of python'

print(challenge.isalnum()) # False # CHecks if the string only includes alphanumeric characters. no spaces or symbols.

print(challenge.isalpha()) # false # Checks if the string comtains only letters.

print(challenge.isdecimal()) # Fa;se # Checks if the string contains only numbers

print(challenge.isdigit())   # False # Checks if the string contains only digits. Differs from decimals in that it takes some codes.

print(challenge.isnumeric()) # False # Checks if the string contains only numbers. Differs form deciamls in that it takes fractions.

print(challenge.islower()) # True # Checks if the string contains only lowercased letters.

print(challenge.isupper())  # False # Checks if th estring contains only uppercased letters.

the_goat = ['Lebron', 'of', 'course']
printed_out = ''.join(the_goat)
print(printed_out)

print(challenge.strip('')) # nothing happens # Removes whatever you put as an argument from the begining and end of the string.

print(challenge.replace('python', 'Rust')) # Replaces a substring with a chosen string.

print(challenge.find('y'))  # 5 # returns the index of the FIRST occurence of your argument, if not found, it returns -1
print(challenge.find('th')) # 0

print(challenge.rfind('y'))  # 16 # returns the  index of the lAST occurence of your arugment, if not found it reutns -1
print(challenge.rfind('th')) # 17

sub_string = 'da'
print(challenge.index(sub_string))  # 7 # returns the index if the FIRST occurence of your argument, retursn an error if not found
# print(challenge.index(sub_string, 9)) # error

print(challenge.rindex(sub_string))  # 7 # returns the index if the LAST  occurence of your argument, retursn an error if not found
# print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19

print(challenge.startswith('fweah')) # False # Checks if the strings starts with your argument.

print(challenge.swapcase()) # THIRTY DAYS OF PYTHON # swtiches the casing of the string.









