import re

pattern = '^[a-zA-Z0-9_]+$'
example1 = 'Roger1_Daltrey_9'
print("Example string 1:", example1)
print(bool(re.match(pattern, example1)))

example2 = 'roger+daltrey'
print("\nExample string 2:", example2)
print(bool(re.match(pattern, example2)))

manual_input = input("\nPlease, input your string: ")


def validation(string):
    if re.match(pattern, string):
        return True
    else:
        return False


print("Matches pattern:", validation(manual_input))
