# an immutable list is called a tuple
# To difine a tuple, we can use parentheses instead of square brackets.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# looping through all values in a tuple
for dimension in dimensions:
    print(dimension)

# although we cannot modify a tuple, we can assign a new value to a variable 
# that holds a tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)