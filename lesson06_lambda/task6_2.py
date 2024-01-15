def correct_list(first_elements, elements_to_delete):
    for element in elements_to_delete:
        first_elements = first_elements.replace(element, "")
    return first_elements
print(correct_list("qwert", ["q", "w", "e"]))
