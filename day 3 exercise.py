age = 19
height_me = 188.5
complex_num = 8-11j
print("Area of the triangle finder:")
base = int(input("What's the base?"))
height = int(input("What's height?"))
print("The area of your traingle =", 0.5 * height * base)
'''
'''
print("Traingle perimeter finder:")
side_a, side_b, side_c = map(float, input("What are the values of the three sides? Seperate with comma plz").split(","))
print("The perimeter =", side_a + side_b + side_c)
'''
'''
print("Area of rectangle finder:")
length, width  = map(float, input("what's the length and width in meter? Seperate with a comma plz").split(","))
print("The area of the rectangle =", length + width, "meters")

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept =-2
x_intercept = -y_intercept / slope

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, x2, y1, y2 = 2, 6, 2, 10
slope2 = (y2-y1)/(x2-x1)
Eucildean_distance = ((x2-x1)**2+(y2-y1)**2)**0.5
print(Eucildean_distance)

#10. Compare the slopes in tasks 8 and 9.

print("does slope1 = slope 2?")
print(slope == slope2)
'''
'''
print(not len("Python")== len("Dragon"))
print("on" in "python" and "on" in "dragon")
print("jargon" in "I hope this course is not full of jargon.")
'''
'''
x = len("python")

x = float(x)
print(x, type(x))

x = str(x)
print(x, type(x))
'''

      #Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python

'''
x = int(input("Even number verifier: enter your number"))
if x % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is NOT even.")
'''

'''
y=7//3
u=int(2.7)
print(y==u)

x=int(9.8)
print(x==10)
'''

'''
print("Salary calculator:")
hours, rate = map(int,input("How many hours do you work and how much dollars do you earn per hour? Seperate each answer with a comma plz").split(","))
weekly_salary, monthly_salary = hours * rate, 4 * hours * rate
print("You earn",weekly_salary,"$ per week, and",monthly_salary,"$ per month")
'''

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
'''
start= int(input("How old are you?"))
how_much_you_got_left = (100-start)*12*30*24*60*60
print("You have",how_much_you_got_left,"seconds left.")


'''
#Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''




print(" 1 1 1 1 1\n 2 1 2 4 8\n 2 1 3 9 27\n 4 1 4 16 64\n 5 1 5 25 125")

