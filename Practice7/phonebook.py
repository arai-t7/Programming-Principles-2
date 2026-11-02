
from connect import connect


def add_contact():
    first_name = input("Enter first name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
            (first_name, phone)
        )
        conn.commit()
        print("Contact added successfully!")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        cur.close()
        conn.close()


def show_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("PhoneBook is empty.")

    cur.close()
    conn.close()



def search_contact():
    print("1. Search by name")
    print("2. Search by phone")

    choice = input("Choose search type: ")

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM contacts WHERE first_name ILIKE %s",
            ('%' + name + '%',)
        )

    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute(
            "SELECT * FROM contacts WHERE phone LIKE %s",
            ('%' + phone + '%',)
        )

    else:
        print("Invalid choice")
        cur.close()
        conn.close()
        return

    rows = cur.fetchall()

    for row in rows:
        print(row)

    if not rows:
        print("Contact not found.")

    cur.close()
    conn.close()

def update_contact():
    phone = input("Enter the current phone number: ")

    print("1. Update first name")
    print("2. Update phone number")

    choice = input("Choose option: ")

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        new_name = input("Enter new name: ")

        cur.execute(
            "UPDATE contacts SET first_name = %s WHERE phone = %s",
            (new_name, phone)
        )

    elif choice == "2":
        new_phone = input("Enter new phone: ")

        cur.execute(
            "UPDATE contacts SET phone = %s WHERE phone = %s",
            (new_phone, phone)
        )

    else:
        print("Invalid choice")
        cur.close()
        conn.close()
        return

    conn.commit()

    if cur.rowcount > 0:
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

    cur.close()
    conn.close()

def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")

    choice = input("Choose option: ")

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")

        cur.execute(
            "DELETE FROM contacts WHERE first_name = %s",
            (name,)
        )

    elif choice == "2":
        phone = input("Enter phone: ")

        cur.execute(
            "DELETE FROM contacts WHERE phone = %s",
            (phone,)
        )

    else:
        print("Invalid choice")
        cur.close()
        conn.close()
        return

    conn.commit()

    if cur.rowcount > 0:
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

    cur.close()
    conn.close()
delete_contact()
import csv
def import_csv():
    conn = connect()
    cur = conn.cursor()

    try:
        with open("contacts.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                cur.execute(
                    """
                    INSERT INTO contacts (first_name, phone)
                    VALUES (%s, %s)
                    ON CONFLICT (phone) DO NOTHING
                    """,
                    (row["first_name"], row["phone"])
                )

        conn.commit()
        print("CSV contacts imported successfully!")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        cur.close()
        conn.close()
def main():
    while True:
        print("\n========== PHONEBOOK ==========")
        print("1. Add contact")
        print("2. Import contacts from CSV")
        print("3. Show all contacts")
        print("4. Search contact")
        print("5. Update contact")
        print("6. Delete contact")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            import_csv()
        elif choice == "3":
            show_contacts()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            delete_contact()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()