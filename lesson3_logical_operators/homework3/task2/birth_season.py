birth_month = input("Введіть номер місяця вашого народження: ")
birth_month_int = int(birth_month)

if birth_month_int in [1,2,12]:
    print("Зима - За вікном падав сніг")
elif birth_month_int in [3,4,5]:
    print("Весна - Все довкола розцвітало")
elif birth_month_int in [6,7,8]:
    print("Літо - Діти насолоджувались літніми канікулами")
elif birth_month_int in [9,10,11]:
    print("Осінь - Все довкола загоралось яскравими фарбами")
else:
    print("Такого місяця не існує")
