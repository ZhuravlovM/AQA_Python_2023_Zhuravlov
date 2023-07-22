#raise Exception('Not supported operation')

def sum(a, b):
    try:
        assert a != b
    except AssertionError as e:
        print('We are in assertion error')
    except TypeError as e:
        print('We are in type error')
    else:
        print('We are in the else statement')
    finally:
        print('Final block of code')
    print('This is code after final')

sum(2, 3)
