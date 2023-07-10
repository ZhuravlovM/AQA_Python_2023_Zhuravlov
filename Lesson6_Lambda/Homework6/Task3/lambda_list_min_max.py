list_1 = [6, 9, 6, 2]
list_2 = [3, 9, 6, 3, 9, 9]
list_3 = [4, 2, 3]

max_length = max(list_1, list_2, list_3, key=lambda x: len(x))
min_length = min(list_1, list_2, list_3, key=lambda x: len(x))

print("Cписок з максимальною довжиною: ", max_length)
print("Спикок з мінімальною довжиною: ", min_length)
