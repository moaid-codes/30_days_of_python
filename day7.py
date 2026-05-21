#                SETS

# Sets are UNORDERED lists of items and ARE mutable.


empty_set = set()  # This is an empty set

print("anything" in empty_set)
empty_set.add("fweah")  # adding 1 item
print(empty_set)

empty_set.update({"playboi", "carti"})  # adding multiple items
print(empty_set)

empty_set.remove("playboi")  # removing an item from the set
print(empty_set)

empty_set.pop()  # removes a RANDOM item from the list and returns it.
print(empty_set)

empty_set.clear()  # clears the entire list.
print(empty_set)

del empty_set  # deletes the whole set

fruits = ["apple", "banana", "orange", "lime"]
fruits = set(fruits)  # Turning a list to a set

print(fruits)
print(type(fruits))

cars = {"lexus", "toyota", "tesla", "BMW"}
print(fruits.union(cars))  # makes a new set with all values from two sets
fruits.update(cars)  # Modifies the OG set and adds the second set's items to it
print(fruits)

print(fruits.intersection(cars))  # Returns shared items from two sets

print(fruits.difference(cars))  # Returns the items UNIQUE to the first set

st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
st2.issubset(st1)  # True # returns true if the first set is a part of the second
st1.issuperset(
    st2
)  # True # returns true if the first set has all values in the second.

print(
    st2.symmetric_difference(st1)
)  # {"item1", "item4"} # makes a set with the values unqie to each set

print(st1.isdisjoint(st2))  # Returns true if both sets don't share a SINGLE value
