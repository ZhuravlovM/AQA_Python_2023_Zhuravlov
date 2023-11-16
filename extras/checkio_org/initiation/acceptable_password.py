"""
In this mission, you need to create a password verification function.
The verification condition is:
 - the length should be bigger than 6.
"""


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

print("The mission is done!")
