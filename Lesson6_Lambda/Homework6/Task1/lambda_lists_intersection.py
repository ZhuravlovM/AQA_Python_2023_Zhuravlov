list_1 = [1, 8, 2, 2, 5, 6]
list_2 = [5, 7, 1, 8, 6, 10]

print("List 1: ", list_1)
print("List 2: ", list_2)

intersection = list(filter(lambda x: x in list_1, list_2))
print("Common numbers: ", intersection)
