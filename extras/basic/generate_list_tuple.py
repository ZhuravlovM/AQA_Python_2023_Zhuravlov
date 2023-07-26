# Write a Python program that accepts a sequence of comma-separated numbers from the user
# and generates a list and a tuple of those numbers

numbers = input("Input some numbers, separated by comma: ")
list = numbers.split(",")
tuple = tuple(list)
print("List: ", list)
print("Tuple: ", tuple)
