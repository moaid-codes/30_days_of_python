



countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



def even_filter(func):
    def wrapper(*args, **kwargs):
        raw_data = func(*args, **kwargs)
        filtered = filter(lambda x: x % 2 == 0, raw_data)
        return filtered
    return wrapper

@even_filter
def _call(x):
    return x

print(list(_call(numbers)))

#print(list(call(numbers)))

for country in countries:
     print(country)


def capitalise(lst):
    result = map(lambda newlst: newlst.upper(), lst)
    return result

print(list(capitalise(countries)))



def square(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        _result = map(lambda s: s * s, result)
        return _result
    return wrapper


@square
def call(x):
    return x

print(list(call(numbers)))



def land_out(x):
    result = filter(lambda x: "land" not in x, x)
    return result

print(list(land_out(countries)))

def pretty_specific(x):
    result = filter(lambda x : len(x) < 6 ,x)
    return result

print(list(pretty_specific(countries)))

def ultra_specific(x):
    result = map(lambda x: x.upper(), (filter(lambda x : x[0] == "E" ,x)))
    return result

print(list(ultra_specific(countries)))


def get_string_lists(lst):
    result = filter(lambda x: isinstance(x, str), lst )
    return result

print(list(get_string_lists(countries)))
