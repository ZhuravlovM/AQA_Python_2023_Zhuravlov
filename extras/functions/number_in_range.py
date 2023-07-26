# Write a Python function to check whether a number falls within a given range

def number_range():
    x = int(input("Enter a number: "))
    if x in range(0, 10):
        print("Number " + str(x) + " is in range")
    else:
        print ("Number " + str(x) + " is not in range")


number_range()
