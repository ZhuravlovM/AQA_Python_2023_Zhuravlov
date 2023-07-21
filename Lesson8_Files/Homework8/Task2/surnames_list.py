with open("names.txt", "w") as f:
    f.write("1, Johnson, UK\n")
    f.write("2, Miles, USA\n")
    f.write("3, Smith, Australia\n")


def make_surnames_list(processed_file):
    surnames_list = []
    with open(processed_file, "r") as file:
        for line in file:
            parted_line = line.strip().split(',')
            surname = parted_line[1].strip()
            surnames_list.append(surname)
    return surnames_list


file_name = "names.txt"
print("Список прізвищ з файлу names.txt:", make_surnames_list(file_name))
