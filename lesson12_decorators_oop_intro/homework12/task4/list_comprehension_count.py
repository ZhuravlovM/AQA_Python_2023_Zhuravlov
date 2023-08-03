import random

random_list = []
for i in range(100):
    random_list.append(random.randint(1, 10))

print("Список випадкових чисел:", random_list)

count_dict = {}
for number in random_list:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

for number, count in sorted(count_dict.items()):
    print(f"Число {number} зустрічається разів: {count}")
