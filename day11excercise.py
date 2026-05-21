import math
import string
from statistics import *
'''
def add_two_numbers(a, b):
    result = a + b
    return result
print(add_two_numbers(5, 2))

def area_of_circcle(r):
    area = math.pi * r ** 2
    area = f"{area:.2f}"
    return area
print(area_of_circcle(5))

def addition(*nums):
    som = 0
    for nums in nums:
        som += nums
    return som
print(addition(5,2,134,14,12,3,12,3,213,21))


def convert_c_to_f(c):
    f = (c * 9 / 5) + 32
    return f
print(convert_c_to_f(12))

def spit_out(a):
    for a in a:
        print(a)
spit_out(['Freddy', 'Bonnie', 'Chica', 'Foxy'])

def reverse(a):
    lst = []
    for a in a:
        lst.insert(0, a)
    return lst
print(reverse([1,2,3,4]))


def capitalize_list_item(*a):
    result = []
    for a in a:
        result.append(string.capwords(a))
    return result
print(capitalize_list_item("hello", "world", "idk", "wth"))

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
def add_item(listo, *x):
    for x in x:
        listo.append(string.capwords(x))
    return listo
print(add_item(food_stuff, "avocado", "dragon fruit", "dates"))

def remote_item(listo, *x):
    for x in x:
        if string.capwords(x) in listo:
            listo.remove(string.capwords(x))
        else:
            pass
    return listo
print(remote_item(food_stuff, "avocado"))

def sum_of_all_numbers(x):
    som = 0
    for x in range(0,x+1):
        som = som + x
    return som
print(sum_of_all_numbers(100))

def sum_of_all_odds(x):
    som = 0
    for x in range(1,x+1,2):
        som = som + x
    return som
print(sum_of_all_odds(5))

def sum_off_all_evens(x):
    som = 0
    for x in range(0,x+1, 2):
        som = som + x
    return som
print(sum_off_all_evens(5))

def evens_and_odds(x):
    evens = 0
    odds = 0
    for x in range(0,x+1,2):
        evens += 1
    for x in range(1,x+1,2):
        odds += 1
    result = f"There are {evens} evens in your number \nand {odds} odds in your number"
    return result
print(evens_and_odds(5))


def factorial(a):
    result = 1
    for a in range(1, a+1):
        result = result * a
    return result

print(factorial(4))

def is_empty(x):
    if not x:
        print("Empty")
        return True
    else:
        print("NOT empty")
        return False
something = "ha"
is_empty(something)

def calculate_mean_median_mode_range_variance_and_std(x):
    _mean = mean(x)
    _median = median(x)
    _mode = mode(x)
    _rang = max(x) - min(x)
    _std = stdev(x)
    _variance = variance(x)
    return f"Whole lotta data:\nthe mean = {_mean}\nthe median = {_median}\nthe mode = {_mode}\nthe range = {_rang}\nthe std = {_std}\nthe variance = {_variance}"
data = [4, 8, 15, 16, 23, 42]
print(calculate_mean_median_mode_range_variance_and_std(data))

def greet(x="Guest"):
    print(f"Hello {string.capwords(x)}!")
greet("lebron james")

def show_args(**x):
    output = ", ".join(f"{key} : {value}" for key,value in x.items())
    return output
print(show_args(name="Lebron", age=40, job="NBA player"))



def is_prime(a):
    if a <= 1:
        print("Nah, it ain't")
        return False
    elif a <= 3:
        print("yeah, it's a prime")
        return True
    y = int(math.sqrt(a)) + 1
    for i in range(2,y):
        if a % i == 0:
            return False
    else:
        return True

print(is_prime(21))


def unique(*x):
    seen = []
    for item in x:
        if item in seen:
            return False
        seen.append(item)
    return True

print(unique("6","5"))


def same_datatype(*x):
    baseline = x[0]
    for x in x:
        if type(baseline) == type(x):
            pass
        else:
            return False
    return True
print(same_datatype(1,2,3))


def valid_name(name):
    if name.isidentifier() == True:
        return True
    else:
        return False

print(valid_name("$something"))

'''

