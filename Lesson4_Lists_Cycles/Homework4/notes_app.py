notes = []

while True:
    action = input("Виберіть дію. Щоб вивести список можливих дій, напишіть 'show': ")

    if action == "show":
        print("add - додати нотатку")
        print("earliest - вивести нотатки у хронологічному порядку (від найновішої до найстарішої)")
        print("latest - вивести нотатки у хронологічному порядку (від найстарішої до найновішої)")
        print("longest - вивести нотатки у порядку довжини (від найдовшої до найкоротшої)")
        print("shortest - вивести нотатки у порядку довжини (від найкоротшої до найдовшої)")
        print("clear - видалити всі нотатки")
        print("exit - вийти з програми\n")

    elif action == "add":
        note = input("Введіть нотатку: ")
        notes.append(note)

    elif action == "earliest":
        print("Від найновішої до найстарішої: ")
        for note in notes:
            print(note)

    elif action == "latest":
        print("Від найстарішої до найновішої: ")
        notes.reverse()
        for note in notes:
            print(note)

    elif action == "longest":
        print("Від найдовшої до найкоротшої: ")
        for note in sorted(notes, key=len, reverse=True):
            print(note)

    elif action == "shortest":
        print("Від найкоротшої до найдовшої")
        for note in sorted(notes, key=len):
            print(note)

    elif action == "clear":
        notes.clear()
        print("Всі нотатки видалено")

    elif action == "exit":
        print("Exit")
        break

    else:
        print("Помилка, спробуйте ще")
