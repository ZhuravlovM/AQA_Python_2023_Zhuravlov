import random

use_generator = input("Do you want to generate minute value? y/n: ")

if use_generator == "Y" or use_generator == "y":
    minute = random.randint(0, 59)
    print("Generated minute is:", minute)
else:
    minute = int(input("Please, enter the minute manually: "))

if minute < 15:
    print(minute, "min - is in the 1st quarter",)
elif minute < 30:
    print(minute, "min - is in the 2nd quarter")
elif minute < 45:
    print(minute, "min - is in the 3rd quarter")
elif minute < 60:
    print(minute, "min - is in the 4th quarter")
else:
    print("Entered value is invalid")


'''
Second option:

minute = random.randint(0, 59)

if minute < 15:
    print(minute,"min - is in the 1st quarter",)
elif minute < 30:
    print(minute,"min - is in the 2nd quarter")
elif minute < 45:
    print(minute,"min - is in the 3rd quarter")
elif minute < 60:
    print(minute,"min - is in the 4th quarter")
'''
