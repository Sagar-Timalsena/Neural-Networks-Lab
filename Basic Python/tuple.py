# Creating a tuple
my_tuple = (1, 2, 3, 'hello', 'world')

# Accessing elements
print("First element:", my_tuple[0])  # Output: 1
print("Last element:", my_tuple[-1])   # Output: 'world'

# Tuple slicing
print("Sliced tuple:", my_tuple[2:5])  # Output: (3, 'hello', 'world')

# Length of the tuple
print("Length of the tuple:", len(my_tuple))  # Output: 5

# Iterating through a tuple
print("Iterating through the tuple:")
for item in my_tuple:
    print(item)

# Nested tuple
nested_tuple = ((1, 2), ('a', 'b'), (True, False))
print("Nested tuple:", nested_tuple)  # Output: ((1, 2), ('a', 'b'), (True, False))

# Tuple unpacking
x, y, z = (10, 20, 30)
print("Unpacked values:", x, y, z)  # Output: 10 20 30

# Tuple as a return value from a function
def get_point():
    return 10, 20

point = get_point()
print("Returned tuple from function:", point)  # Output: (10, 20)

# Tuple with one element
single_tuple = (5,)
print("Single element tuple:", single_tuple)  # Output: (5,)
