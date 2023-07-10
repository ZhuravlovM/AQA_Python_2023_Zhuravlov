number_check = lambda x: x.replace('.', '', 1).isdigit()

print(number_check("HelloWorld"))
print(number_check("123123"))
print(number_check("23.4"))


'''
# Second option
number_check = lambda x: x.replace('.', '', 1).isdigit()
manual_enter = input("Введіть дані: ")
result = number_check(manual_enter)

if result:
    print("Цей рядок є числом")
else:
    print("Цей рядок не є числом")
'''
