my_list = ['alphabet', 'doorbell', 'axis', 'bootleg', 'zookeeper']
new_list = []

for element in my_list:
    if element.startswith('a'):
        new_list.append(element)

print(new_list)
