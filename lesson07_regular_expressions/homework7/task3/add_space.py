import re

pattern = '([A-Z])'

user_input = input("Введіть слова з великими літерами без пробілів між ними: ")
processed_string = re.sub(pattern, r' \1', user_input)
print(processed_string)
