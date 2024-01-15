import random

'''
list_of_numbers = [5,8,3,4,8,1,3,7,4,3]
list_of_numbers2 = []
for element in list_of_numbers:
    element = element + 5
    list_of_numbers2.append(element)
#    print(element)
#print(list_of_numbers2)
#new_list_of_numbers = list_of_numbers.copy()
new_list_of_numbers = list(list_of_numbers)
for i in range(len(list_of_numbers)):
    list_of_numbers[i] = list_of_numbers[i] + 5
print(list_of_numbers)

print(new_list_of_numbers)

new_list_of_numbers = list_of_numbers + new_list_of_numbers
print(new_list_of_numbers)
print(new_list_of_numbers.count(10))
new_list_of_numbers.reverse()
print(new_list_of_numbers)
new_tuple = (1,2,3)

for element in new_tuple:
    print(element)

while len(new_list_of_numbers) > 5:
    new_list_of_numbers.pop()
    print(new_list_of_numbers)

counter = 0
while counter < 10:
    new_list_of_numbers.append(counter)
    counter +=1   # counter = counter + 1
print(new_list_of_numbers)

'''

'''
while counter < 10:
    a = random.randint(1,10)
    print('aaaaa')
    print(a)
    if a == 10
        continue
    counter +=2
'''

'''
for element in new_list_of_numbers:
    if element == 8:
        print("We're in continue block")
        continue
    print(element)
'''

'''
value = 0
while True:
    value_temporary = input('Print: ')
    if value_temporary == "sum":
        break
    elif value_temporary.isnumeric():
        value += int(value_temporary)
    else:
        print("You input wrong word")
        continue
print(value)
'''
