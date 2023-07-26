with open("names.txt", "w") as text_file:
    text_file.write("1, Johnson, UK\n")
    text_file.write("2, Miles, USA\n")
    text_file.write("3, Smith, Australia\n")


def make_surnames_list(processed_file):
    surnames_list = []
    with open(processed_file, "r") as file:
        for line in file:
            parted_line = line.strip().split(',')
            surname = parted_line[1].strip()
            surnames_list.append(surname)
    return surnames_list


file_name = "names.txt"
surnames = make_surnames_list(file_name)
print("Список прізвищ з файлу names.txt:")
print(surnames)
