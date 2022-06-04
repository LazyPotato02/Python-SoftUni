def phone_book_information(number_of_lines, phone_book):

    for x in range(number_of_lines):
        name = input()
        if name not in phone_book:
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {phone_book[name]}")

    return True


def phonebook():
    contacts = {}

    condition = False

    while True:
        contact = input().split('-')

        if contact[0].isdigit():
            condition = phone_book_information(int(contact[0]), contacts)
        else:
            contacts[contact[0]] = contact[1]

        if condition:
            break

phonebook()