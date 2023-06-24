import math
import random

one = 2        # int
g_value = 9.8  # float
message = 'This is message'  # string
result = True  # boolean
empty_result = None  # NoneType

'''
print(one)
print(type(one))
print(id(one))
print(id(g_value))
print(id(empty_result))
'''

'''
print(id(one))
one = g_value
print(id(one))
print(id(g_value))
'''

'''
first_value = 2
second_value = 4
third_value = first_value + second_value
print(third_value)
print(third_value - first_value)
print(first_value * second_value)
print(first_value / second_value)
print(first_value // second_value)  # Floor division
print(first_value % second_value)   # Modulus
print(3**2)                         # Exponentiation
print(3**3)
print(2 + 3 * 4)
print((2+3) * 4)
print(0.1 * 0.1)
small_number = 0.1 * 0.1
print(round(small_number,  2))
'''

'''
print(math.pi)
pi = math.pi
r = 2
print(pi * r**2)
print(math.cos(2))
'''

'''
random_number = random.randint(1,50)
pi = math.pi
print(random_number)
print(pi * random_number**2)
print(random.randrange(15))
print(random.choice(['god exists', 'you exist']))
'''


print(dir('aaaa'))    # 'dir' returns all available methods allowed for this value type
my_name = 'my name'
#print(my_name.title())
#print(my_name.upper())
#print(my_name.lower())
first_name = 'Batman'
second_name = 'Joker'
full_name = first_name + ' ' + second_name
print("Hello, " + full_name)
print('\tpython')
print("Hello, my name is " + full_name + "\nand I'm here \nto learn python")


first_string = ' Python'
second_string = 'python '
print(second_string.rstrip())   # deletes spaces on the right
print(first_string.lstrip())    # deletes spaces on the left

company_info = 'amazon amazon is a very huge company, unfortunately'
#print(company_info.capitalize())    # writes fisrt letter of sentence as a capital
#print(company_info.replace('amazon', 'Apple'))
#print(company_info.replace('amazon', 'Apple', 1))

print('is' in company_info)
print(company_info.islower())
print(company_info.isupper())
print(first_name.isalpha())
print(' '.isspace())
print('4'.isdigit())
four_alpha = '4'
four_numeric = 4
print(company_info.count('amazon'))    # counts how many times this value appears
print(company_info.index('a'))    # shows location in the string, returns error if nothing found
print(company_info.find('a'))     # -n- returns -1 if nothing found
print(len(company_info))    # counts number of elements in the string
print(company_info.split())    # splits a string into a list, default separator is any whitespace
print('this is firt line \nthis is second line'.splitlines())
print(company_info[21])
print(company_info[21:])
print(company_info[21:30])
print(company_info[:30])
print(company_info[21:30:2])

food = 'solyanka'
price = 90
print('Food is {} and price is {}'.format(food, price))
print(f'food is {food}, price is {price}')