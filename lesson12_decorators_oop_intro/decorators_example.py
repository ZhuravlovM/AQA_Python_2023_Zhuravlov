import datetime


def percent(func):
    def inner(*args, **kwargs):
        header, footer = "%"*20, "%"*20
        return f"{header}\n{func(*args, **kwargs)}\n{footer}"
    return inner


def and_symbol(func):
    def inner(*args, **kwargs):
        header, footer = "&"*20, "&"*20
        return f"{header}\n{func(*args, **kwargs)}\n{footer}"
    return inner


def add_footer_header(sign, quantity):
    def middle_level(func):
        def inner(some_msg):
            footer = sign * quantity
            header = sign * quantity
            return f"{header}\n{func(some_msg)}\n{footer}"
        return inner
    return middle_level


#@and_symbol
#@percent
@add_footer_header(sign="#", quantity=10)
def hi(msg):
    return "***\n$$$\n" + msg + "\n$$$\n***"


print(hi('hello my fellow friends'))


def timer_function(func):
    def timer(*args, **kwargs):
        start = datetime.datetime.now()
        result_function = func(*args, **kwargs)
        end = datetime.datetime.now()
        print(end - start)
        return result_function
    return timer


@timer_function
def mega_math(first_value, second_value):
    for i in range(10000):
        first_value * second_value
        return 'done'


print(mega_math(5, 10))

