# basic print programs in python
print("hello world")

print(3*3)
print(45/5)
print(3%2)
print(45**2)

# list
# Ordered
# Mutable
# Allows duplicates
# Indexed
# Uses []
fruits = ["mango", "banana", "orange", 1, 9.9]
fruits[2] = "strewberry" 
fruits.append("orange")
fruits.remove("mango")
print(fruits)

# tuple
# Ordered
# Immutable
# Allows duplicates
# Indexed
# Uses ()
coordinates = (10,20)
print(coordinates[0])
numbers = (1,2,3,4,5,6)
print(numbers[5])
address = (28, "st. John's street")
print(address)

# set
# No duplicates
# Mutable (you can add or remove items)
# Not indexed
# Unordered
# Uses {}
fruits = {"apple", "apple", "banana", "banana"}
fruits.remove("apple")
print(fruits)
numbers = {1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5}
numbers.add(6)
print(numbers)

# dictionary 
# Store data as key-value pairs
# Mutable
# Keys are unique
# Values can repeat
# Access values by key instead of index
# Use {}
student = {
    "name": "John",
    "age": 75,
    "course": "computer science",
}
# adding new data to a dictionary
student["country"] = "Nigeria"
# changing a data in a dictionary
student["age"] = 80
print(student)


# varible type
print(type(10))
print(type("john"))
print(type(4.5))
print(type(True))
print(type([1,23,45,60]))
print(type({'name': 'john'}))
print(type({4,5,4,54,4,4}))
print(type({7.8,89.0, 56.8}))