import random
import string
'''
def random_user_id():
    pool = string.ascii_letters + string.digits
    lst = random.choices(pool, k=6)
    user_ID = "".join(lst)
    return user_ID

print(random_user_id())
'''
'''
def input_user_id():
    pool = string.ascii_letters + string.digits
    characters, IDs = input("How many characters and IDs? Seperate with a comma.  Example: 5, 2\n").split(',')
    characters = int(characters)
    IDs = int(IDs)
    count = 0
    while count < IDs:
        lst = random.choices(pool, k=characters)
        user_ID = "".join(lst)
        print(user_ID)
        count = count + 1
input_user_id()

'''
'''
def rgb_color_gen(count = 3):
    pool = string.digits
    lst = {"".join(random.choices(pool, k=3)) for _ in range(count)}
    print(f"rgb({', '.join(lst)})")
rgb_color_gen()

def list_of_hexa_colors(number):
    result = []
    for number in range(number+1):
        pool = string.digits + string.ascii_lowercase[:6] + string.ascii_uppercase[:6]
        print(type(random.choices(pool, k=6)))
        color = "#" + "".join(random.choices(pool, k=6))
        result.append(color)
    return result
print(list_of_hexa_colors(5))


def shuffler(x):
    copy = x
    random.shuffle(copy)
    return copy
something = [1,2,3,4,5,6]
print(shuffler(something))
'''

'''

def seven_unique_number():
    pool = string.digits
    attempt_1 = random.choices(pool, k=7)
    while len(set(attempt_1)) != len(attempt_1):
            new_numbers = 7 - len(set(attempt_1))
            attempt_1 = attempt_1 + list(random.choices(pool, k=new_numbers))
    return attempt_1
print(seven_unique_number())

'''
def seven_unique_number():
    pool = string.digits
    attempt_1 = random.choices(pool, k=7)
    while len(set(attempt_1)) != len(attempt_1):
            new_numbers = 7 - len(set(attempt_1))
            attempt_1 = list(set(attempt_1)) + list(random.choices(pool, k=new_numbers))
    return attempt_1
print(seven_unique_number())


