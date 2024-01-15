import random

'''
a = input("Please write here input value: ")    # output is string value
print(a)

a = input("Please write here integer: ")
integer_value_a = int(a)
print(a)
'''

'''
this_is_true = True
this_is_true_integer = int(this_is_true)    # converts True/False into 1/0
print(this_is_true)
this_is_empty_string = ''                   # returns False if empty
print(bool(this_is_empty_string))
'''

# < less
# > more
# <= less or equal
# >= more or equal
# == equal
# != not equal

'''
a = input("Please, insert 'a': ")
a_int = int(a)
if a_int > 5:
    print("Congratulations, you win")
elif a_int < 3:
    print("Try harder")
else:
    print("Better luck next time")


first_value = 20
if first_value > 15 or first_value < 25:
    print("It's around 20")

#if type(first_value) == int or first_value < 25:
#    print("It's around 20")

second_value = 15
if second_value <= 16 and second_value > 10:
    print("It's around 13")
else:
    print("Number is invalid")

print(bool(0))
print(bool(1))

third_value = 5
if third_value > 4 and not second_value > 20:
    print("a")
'''

'''
eyes = int(input("Number of eyes: "))
legs = int(input("Number of legs: "))
if eyes == 8:
    if legs == 8:
        print("This is a spider")
    elif legs == 6:
        print("This is a fly")
    else:
        print("Creature is undefined")
elif eyes > 1 and eyes < 8:
    print("Meet the horror beyond your comprehensions")
elif eyes == 1:
    print("This is Odin or Cyclopus")
'''

'''
int1 = int(input("Take a card "))
int2 = random.randint(2, 14)
if int1 == 1:
    print("Card was chosen")
    if int2 > 13:
        print("Ace")
    elif int2 > 12:
        print("King")
    elif int2 > 11:
        print("Queen")
    elif int2 > 10:
        print("Jack")
    else:
        print("10 or less")
elif int1 == 0:
    print("Card wasn't chosen")
'''

'''
our_beautiful_list = [2,3,4,5,8,"item",9.0]
our_list_1 = []
our_list_2 = list()
print(len(our_beautiful_list))
print(our_beautiful_list[1])
print(our_beautiful_list[-1])
print(our_beautiful_list.index(3))
our_beautiful_list.append(8)
print(our_beautiful_list)
our_beautiful_list.insert(3, 11)
print(our_beautiful_list)
our_beautiful_list.remove("item")
print(our_beautiful_list)
our_beautiful_list.pop(0)   # removes item by index
print(our_beautiful_list)
del our_beautiful_list[1]
print(our_beautiful_list)
our_beautiful_list.clear()  # clears our list
print(our_beautiful_list)
'''

another_list = [9,3,4,1,6,5,7,2]
simple_list = [1,2,3]
another_list.sort(reverse = True)
print(another_list)
print(another_list[:5])
print(another_list[1:])
another_list.extend(simple_list)
print(another_list)
