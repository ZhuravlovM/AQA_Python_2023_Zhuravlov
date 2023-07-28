from datetime import datetime, timedelta


def add_subtrack_time(date, days, operation):
    if operation:
        date_calculated = date + timedelta(days=days)
    else:
        date_calculated = date - timedelta(days=days)
    return date_calculated


date_input = input("Введіть поточну дату та час у форматі 'YYYY-MM-DD HH:MM:SS': ")
current_date_value = datetime.strptime(date_input, __format="%Y-%m-%d %H:%M:%S")

days_value = int(input("Введіть кількість днів для додавання або віднімання: "))

while True:
    operation_input = input("Оберіть операцію додавання або віднімання +/- : ")
    if operation_input == "+":
        is_addition = True
        break
    elif operation_input == "-":
        is_addition = False
        break
    else:
        print("Значення невірне, спробуйте ще раз")

new_date = add_subtrack_time(current_date_value, days_value, is_addition)
print(new_date)
