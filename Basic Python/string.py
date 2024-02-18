'''
lenth of string (len(str))


str = "Sagar Timalsena"
print(str[1: 13])
          ^  ^
          1 is starting index and 13 last index
          (Last index len(str))
          [:] -> o to last index 
'''
'''
          Slicing 
          Negative index
          counting backward starting from -1 
          eg -1 -2 -3 -4 -5 -6 

          str = "Sagar Timalsena"
print(str[-15: -1])
print(len(str))

'''
'''
          String Function 
          str.

'''

'''
str = "Hello coder Boy"

# Return true if string ends with substr
print(str.endswith("Boy"))  # Output: True

# Capitalize 1st char
print(str.capitalize())  # Output: Hello coder boy

# Replace all occurrences of old and new character
print(str.replace('l','s'))  

# Find the 1st index of 1st occurrence
print(str.find("Hello"))  # Output: 0

# Count the occurrences of the substr
print(str.count("ll"))  # Output: 1

'''
'''
          conditional Statements
          if-elif-else

          if(condition):
                    statement 1
          elif(condition):
                    statement 2

'''

age  = 21

if(age >= 18):
          print("Love your sister")

elif(age <= 18):
          print("Love your mom")
