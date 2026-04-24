# Phone Book Application

phone_book = {
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla"
}


def is_valid_number(number):
    """Check if the phone number is valid (10 digits only)."""
    return number.isdigit() and len(number) == 10


def find_name_by_number():
    phone_number = input("Enter the phone number: ")

    if not is_valid_number(phone_number):
        print("Invalid phone number.")
        return

    if phone_number in phone_book:
        print(f"Name: {phone_book[phone_number]}")
    else:
        print("Number not found.")


def find_number_by_name():
    name = input("Enter the name: ")

    for number, owner in phone_book.items():
        if owner.lower() == name.lower():
            print(f"Phone Number: {number}")
            return

    print("Name not found.")


def add_new_contact():
    name = input("Enter new name: ")
    number = input("Enter new number: ")

    if not is_valid_number(number):
        print("Invalid phone number.")
        return

    phone_book[number] = name
    print("Contact added successfully!")


def main():
    print("📱 Phone Book Application")

    while True:
        print("\n1. Find name by number")
        print("2. Find number by name")
        print("3. Add new contact")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            find_name_by_number()
        elif choice == "2":
            find_number_by_name()
        elif choice == "3":
            add_new_contact()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
