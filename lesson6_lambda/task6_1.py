def find_number_in_range(number, max_range, min_range=0):
    if number > min_range and number < max_range:
        return True
    else:
        return False

print(find_number_in_range(7, 6, 2))
