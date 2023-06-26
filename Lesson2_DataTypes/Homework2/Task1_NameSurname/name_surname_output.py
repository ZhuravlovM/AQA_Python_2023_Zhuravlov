# Subtask1
first_name = "Mykyta"
last_name = "Zhuravlov"

full_name = first_name + " " + last_name
print("My full name is " + full_name)

print("Lowercase: " + full_name.lower())
print("Uppercase: " + full_name.upper())

# Subtask2
lowercase_name = full_name.lower()
print("Capital letters: " + lowercase_name.title())

# Subtask3
name_with_spaces = "\n\t" + full_name + "\t"
print(name_with_spaces + "is my name with spaces\n")
print(name_with_spaces.strip() + " - is printed with strip")
print(name_with_spaces.lstrip() + " - is printed with lstrip")
print(name_with_spaces.rstrip() + " - is printed with rstrip")
print(name_with_spaces.replace("\t","").replace("\n","").replace(" ","") + " - is printed with replace")