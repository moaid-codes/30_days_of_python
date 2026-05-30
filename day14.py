#               HIGHER ORDER FUNCTIONS
import time
import string
'''
def sum_numbers(x):
    return sum(x)

def higher_order_function(f, lst):
    result = f(lst)
    return result

print(higher_order_function(sum_numbers, [1,2,3,4,G])

'''
'''
higher_order_function = map(capitalize, lst)
print(higher_order_function)

'''


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"This function took {end - start:.4f} seconds to run.")
        return result
    return wrapper


lst = ["sweden", "britain", "mexico", "japan"]


def capitalize(func):
    def wrapper():
        result = func()
        print("\nunboxing the wrapping")
        result = list(map(string.capwords, result))
        something = sum(i**2 for i in range(1000000))
        print("This prints out AFTER the capitalize result was made.")
        return result
    return wrapper

@timer
@capitalize
def name_fetcher():
    x = lst
    return x

print(name_fetcher())



@timer
def heavy_calculation():
    return sum(i**2 for i in range(1000000))

heavy_calculation()





def even_number_filter(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        filtered = filter(lambda x: x % 2 == 0, data)
        return filtered
    return wrapper
@even_number_filter
def call(x):
    return x

x = [1,2,3,4,5,6,7,8,9,10]
print(list(call(x)))

