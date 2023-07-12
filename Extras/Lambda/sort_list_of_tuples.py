# Write a Python program to sort a list of tuples using Lambda

parts_price = [('rim', 50), ('brake pads', 15), ('coolant', 18), ('clips', 4)]
print("Original:", parts_price)
parts_price.sort(key= lambda x: x[1])
print("Sorted:", parts_price)
