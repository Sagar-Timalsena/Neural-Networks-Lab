
# i = 1
# while i <= 20:
#     print(i)
#     i += 1


# palindrome 

# def is_palindrome(s):
#     # Remove spaces and convert to lowercase
#     s = s.replace(" ", "").lower()
    
#     # Check if the string is equal to its reverse
#     return s == s[::-1]

# # Test the function
# string = input("Enter a string: ")
# if is_palindrome(string):
#     print("Yes, it's a palindrome!")
# else:
#     print("No, it's not a palindrome.")

# odd even 
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
num = int(input("Enter a number: "))
result = check_odd_even(num)
print(f"The number {num} is {result}.")

