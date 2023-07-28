def print_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Text in '{filename}':", content)
    except FileNotFoundError as error:
        print(f"File '{filename}' not found")
    else:
        print("File printed successfully")
    finally:
        print("Function completed")


print_file("non_existent.txt")

print("\nCalling function one more time\n")

print_file("file_example.txt")
