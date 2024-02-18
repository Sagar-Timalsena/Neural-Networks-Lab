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

'''
age  = 21

if(age >= 18):
          print("Love your sister")

elif(age <= 18):
          print("Love your mom")
          
'''
'''
marks = int(input("Enter the bus number:"))

if(marks >=90):
          grade = "A"
elif(marks >=70):
          grade = "B"
elif(marks >=70):
          grade = "C"
else: 
        grade = "D"

print("Grade of the Bus  is ", grade)
'''
# Program to check even or odd
'''
number = int(input("Enter the number: "))
if(number % 2 == 0):
          print("Even Number")
else:
        print("Odd Number")

'''

'''

# find the greatest of 3 numbers entered by the user

num1 = int(input("Enter your 1st number:"))
num2 = int(input("Enter your 2st number:"))
num3 = int(input("Enter your 3st number:"))

if(num1 >= num2 and num2 >= num3):
          print("First number is largest", num1)
if(num2 >= num3):
        print("Second number is largest", num2)
else:
        print("third number is largest", num3)
        
'''

'''
check if a given number is multiple of 7 or not

userinput = int(input("Enter any number: "))

if(userinput % 7 == 0):
          print(" The Given Number is divided by 7 and remainder was 0")
else:
        print("Fuck this number")

        '''
