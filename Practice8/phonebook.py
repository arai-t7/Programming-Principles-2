from connect import connect


# 1. Search contacts
def search_contacts():
    pattern = input("Enter name or phone to search: ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "SELECT * FROM get_contacts_by_pattern(%s)",
            (pattern,)
        )

        results = cur.fetchall()

        if results:
            for contact in results:
                print(contact)
        else:
            print("No contacts found.")

    finally:
        cur.close()
        conn.close()


# 2. Insert or update contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "CALL upsert_contact(%s, %s)",
            (name, phone)
        )

        conn.commit()
        print("Contact successfully added or updated!")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        cur.close()
        conn.close()


# 3. Insert many contacts
def insert_many_contacts():
    names = input("Enter names separated by commas: ").split(",")
    phones = input("Enter phones separated by commas: ").split(",")

    names = [name.strip() for name in names]
    phones = [phone.strip() for phone in phones]

    if len(names) != len(phones):
        print("Error: Names and phones must have equal length.")
        return

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "CALL insert_many_contacts(%s, %s, %s)",
            (names, phones, None)
        )

        result = cur.fetchone()
        conn.commit()

        if result and result[0]:
            print("Incorrect data:")
            print(result[0])
        else:
            print("All contacts processed successfully!")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        cur.close()
        conn.close()


# 4. Pagination
def show_contacts():
    limit = int(input("How many contacts to show? "))
    offset = int(input("How many contacts to skip? "))

    if limit <= 0 or offset < 0:
        print("Invalid limit or offset.")
        return

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "SELECT * FROM get_contacts_paginated(%s, %s)",
            (limit, offset)
        )

        results = cur.fetchall()

        for contact in results:
            print(contact)

        if not results:
            print("No contacts found.")

    finally:
        cur.close()
        conn.close()


# 5. Delete contact
def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter name: ")
        params = (name, None)

    elif choice == "2":
        phone = input("Enter phone: ")
        params = (None, phone)

    else:
        print("Invalid choice.")
        return

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "CALL delete_contact(%s, %s)",
            params
        )

        conn.commit()
        print("Delete operation completed!")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        cur.close()
        conn.close()


# Main menu
def main():
    while True:
        print("\n========== PHONEBOOK ==========")
        print("1. Search contacts")
        print("2. Add or update contact")
        print("3. Insert many contacts")
        print("4. Show contacts (Pagination)")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            search_contacts()

        elif choice == "2":
            add_contact()

        elif choice == "3":
            insert_many_contacts()

        elif choice == "4":
            show_contacts()

        elif choice == "5":
            delete_contact()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()