def print_fullname(firstname = "lil", lastname = "bro"):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname()
print_fullname(firstname = 'Fweah', lastname = 'carti')

def addition(a,b):
    result = a + b
    print(result)
addition(10,12)

def can_u_drive(b,c):
    age = c - b
    if age>18:
        print("yeah")
        return True
    print("nah")
    return False
can_u_drive(2008,2026)

