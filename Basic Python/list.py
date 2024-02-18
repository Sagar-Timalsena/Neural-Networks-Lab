# A built in data types that stores set of values, it can also store elements of different types(int,str,float etc.)
# string are immutable (cannot change)
# lists  are mutable (can change)

# Define a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print("First element:", my_list[0])  # Output: 1
print("Last element:", my_list[-1])   # Output: 5

# Modifying elements
my_list[0] = 10
print("Modified list:", my_list)  # Output: [10, 2, 3, 4, 5]

# Appending elements
my_list.append(6)
print("After appending 6:", my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Inserting elements
my_list.insert(2, 7)
print("After inserting 7 at index 2:", my_list)  # Output: [10, 2, 7, 3, 4, 5, 6]

# Removing elements
my_list.remove(4)
print("After removing 4:", my_list)  # Output: [10, 2, 7, 3, 5, 6]

# Popping elements
popped_element = my_list.pop()
print("Popped element:", popped_element)  # Output: 6
print("List after popping:", my_list)     # Output: [10, 2, 7, 3, 5]

# Slicing
sliced_list = my_list[1:4]
print("Sliced list:", sliced_list)  # Output: [2, 7, 3]

# Length of the list
print("Length of the list:", len(my_list))  # Output: 5

# Sorting
my_list.sort()
print("Sorted list:", my_list)  # Output: [2, 3, 5, 7, 10]

# Reversing
my_list.reverse()
print("Reversed list:", my_list)  # Output: [10, 7, 5, 3, 2]

# Clearing the list
my_list.clear()
print("Cleared list:", my_list)  # Output: []
