
from connect import connect


def add_phone():
    name = input("Enter full contact name: ")
    phone = input("Enter phone number: ")
    phone_type = input("Enter phone type (mobile/home/work): ")

    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute(
            "CALL add_phone(%s, %s, %s)",
            (name, phone, phone_type)
        )
        conn.commit()
        print("Phone added successfully!")

    except Exception as error:
        conn.rollback()
        print("Error:", error)

    finally:
        conn.close()


def move_to_group():
    name = input("Enter contact name: ")
    group = input("Enter group name: ")

    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute(
            "CALL move_to_group(%s, %s)",
            (name, group)
        )
        conn.commit()
        print("Contact moved successfully!")

    except Exception as error:
        conn.rollback()
        print("Error:", error)

    finally:
        conn.close()


def search_contacts():
    query = input("Enter name, email or phone: ")

    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM search_contacts(%s)",
            (query,)
        )

        results = cur.fetchall()

        if results:
            for contact in results:
                print(contact)
        else:
            print("No contacts found.")

    except Exception as error:
        print("Error:", error)

    finally:
        conn.close()


def main():
    while True:
        print("\n===== PHONEBOOK =====")
        print("1. Add phone")
        print("2. Move contact to group")
        print("3. Search contacts")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_phone()
        elif choice == "2":
            move_to_group()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
