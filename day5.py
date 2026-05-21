

#               LISTS

important = "Lists are modifiable and DO retain order"

fruits =["apple", "banana", "mange", "lemon", "lime", "something"]
first_fruit, second_fruit, *three_in_the_middle, so = fruits # assigning variables to values in a list
print(three_in_the_middle, so)

fruits[4] = "avocado" # modifying a list
print(fruits)
verifier = "apple" in fruits
print(verifier)

fruits.insert(1,"orange")   # Adding items to a list
print(fruits)

fruits.remove("lemon") # Removing items form a list
print(fruits)

fruits.pop() # Removes the value at the last index
print(fruits)
fruits.pop(0) # Removes the value at the specified index
print(fruits)

cars = ["toyota", "BMW", "telsa", "mercedes", "lexus"]
del cars[1] # deletes the value at the specified index
print(cars)
del cars[1:3] # deletes the indexes in a range. It does NOT reach three
cars_backup = cars.copy()
print(cars)
del cars # deletes the whole list

fruits_backup = fruits.copy()  # Makes a copy list of an original list

fruits_backup.clear() # clears all values in a list and makes it empty
print(fruits_backup)

cars_and_fruits = fruits + cars_backup # you can join lists by making a new list
print(cars_and_fruits)

fruits.extend(cars_backup) # you can also join lists by extending one onto the other
print(fruits)

print(fruits.count("lexus")) # counts the occurences of a value in your list

print(fruits.index("orange")) # finds the index of the specified variable

fruits.reverse() # Reverses the list
print(fruits)

fruits.sort()   # Sorts the list in acending Alphabetical order. If it we're digits it would be in acending numeric order.
print(fruits)

fruits.sort(reverse=True)   # Reverses the order
print(fruits)
