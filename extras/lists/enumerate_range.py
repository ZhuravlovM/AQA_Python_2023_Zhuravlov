my_list = ['elephant', 'tiger', 'parrot', 'whale', 'eagle']
new_list = []

for index, element in enumerate(my_list):
    if index % 2 == 0:
        new_list.append(element)
    else:
        new_list.append(element[::-1])

print(new_list)

#############################################################

my_list2 = ['elephant', 'tiger', 'parrot', 'whale', 'eagle']
new_list2 = []

for index in range(len(my_list2)):
    if index % 2 == 0:
        new_list2.append(my_list2[index])
    else:
        new_list2.append(my_list2[index][::-1])

print(new_list2)
