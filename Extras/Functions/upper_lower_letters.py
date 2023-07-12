# Write a Python function that accepts a string and counts the number of upper and lower case letters

def accept_string(sentence):
    uppers = 0
    lowers = 0
    for x in sentence:
        if x.islower():
            lowers += 1
        elif x.isupper():
            uppers += 1
    return uppers, lowers


print(accept_string("Hello, Mr Jones! Weather is good today."))
