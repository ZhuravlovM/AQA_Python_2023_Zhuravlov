# Write a Python program to select a random element from a list, set, dictionary-value.
# Use random.choice()

import random

list_example = []
for i in range(10):
    list_example.append(random.randint(1, 10))

set_example = {1, 2, 3, 'four', 'five'}

dict_example = {'name': 'Roberto', 'city': 'Dallas', 'country': 'USA'}


list_element = random.choice(list_example)
print("Element from list:", list_element)

set_element = random.choice(list(set_example))
print("\nElement from set:", set_element)

key_element = random.choice(list(dict_example.keys()))
value_element = dict_example[key_element]
print("\nElement from dict:", "\nKey:", key_element, "\nValue:", value_element)
