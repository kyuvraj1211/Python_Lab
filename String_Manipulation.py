# Take a string input from the user
user_string = input("Enter a string: ")

#Prints the first 3 characters
print("First 3 characters:", user_string[:3])

#Prints the last 2 characters
print("Last 2 characters:", user_string[-2:])

#Prints the string with every second character
print("Every second character:", user_string[::2])

#Prints the string in reverse using slicing
print("Reversed string:", user_string[::-1])
