x = float(input("Введіть значення координати Х: "))
y = float(input("Введіть значення координати Y: "))

if x == 0 and y == 0:
    print(f"Точка ({x},{y}) лежить на початку координат")
elif x == 0:
    print(f"Точка ({x},{y}) лежить на осі X")
elif y == 0:
    print(f"Точка ({x},{y} лежить на осі Y")

if x > 0 and y > 0:
    print(f"Точка ({x},{y}) знаходиться у I-й координатній чверті")
elif x < 0 and y > 0:
    print(f"Точка ({x},{y}) знаходиться у II-й координатній чверті")
elif x < 0 and y < 0:
    print(f"Точка ({x},{y}) знаходиться у III-й координатній чверті")
elif x > 0 and y < 0:
    print(f"Точка ({x},{y}) знаходиться у IV-й координатній чверті")
