# Program przechowujący danę kontaktowe znajomych/klientów.
#
# Program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie. Zadania to:
# Wyświetlenie wszystkich wpisów
# Stworzenie nowego wpisu (dane wczytywane z klawiatury)
# Usunięcie wpisu
# Zakończenie pracy programu
# Program powinien na starcie mieć już wprowadzone kilka wpisów.
contacts = []
def display_menu():
    print("1. Display all contacts")
    print("2. Add a new contact")
    print("3. Delete a contact")
    print("4. Quit the program")
def display_all_contacts():
    if not contacts:
        print("No available contacts.")
    else:
        for contact in contacts:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print()
def add_new_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print("New contact added!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("Contact deleted!")
            return
    print("Contact not found.")
def main():
    print("Welcome to the contact management program!")
    display_menu()

    while True:
        choice = input("Select an option (1-4): ")

        if choice == "1":
            display_all_contacts()
        elif choice == "2":
            add_new_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
