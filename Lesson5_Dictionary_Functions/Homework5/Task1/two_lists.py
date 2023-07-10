from random import randint

list_1 = []
list_2 = []
for i in range(10):
    list_1.append(randint(1, 10))
    list_2.append(randint(1, 10))

print("List 1:", list_1)
print("List 2:", list_2)

def common_numbers(list_1,list_2):
    common = set(list_1) & set(list_2)
    sorted_result = sorted(common)
    for numbers in sorted_result:
        print(numbers)


print('\nCommon numbers in ascending order:')
common_numbers(list_1, list_2)
