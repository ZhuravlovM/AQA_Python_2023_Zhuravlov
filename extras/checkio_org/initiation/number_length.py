# You have a non-negative integer. Try to find out how many digits it has.


def number_length(value: int) -> int:
    return len(str(value))


print("Example:")
print(number_length(100))

# These "asserts" are used for self-checking
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

print("The mission is done!")
