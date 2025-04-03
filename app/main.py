import sqlite3
import datetime

DB_PATH = "database/library.db"

def connect_db():
    return sqlite3.connect(DB_PATH)

def view_items():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Item")
        items = cursor.fetchall()
        print("\n All Library Items: ")
        for item in items:
            item_id, title, item_type, fmt, available, date_added, price = item
            status = "Yes" if available else "No"
            print(f"ID: {item_id} | Title: {title} | Type: {item_type} | Format: {fmt} | Available: {status} | Date Added: {date_added} | Price: ${price}")
        
        input("Press Enter to return to main menu..")
        
def search_items():
    while True:

        keyword = input("Enter a keyword to search (or 0 to return to main menu): ")
        
        if keyword == "0":
            print("Returning to main menu")
            return
        
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Item WHERE title LIKE ?", ('%' + keyword + '%',))
            results = cursor.fetchall()
            if results:
                print("\n Search Results:")
                for item_id, title, item_type, fmt, available, date_added, price in results:
                    status = "Yes" if available else "No"
                    print(f"ID: {item_id} | Title: {title} | Type: {item_type} | Format: {fmt} | Available: {status} | Date Added: {date_added} | Price: ${price}")
                
                again = input("\n Search again? (y/n): ").lower()
                if again != 'y':
                    print("Returning to main menu.")
                    return
            else:
                print("No items found.")

def borrow_item():
    while True:
        try:
            member_input = input("Enter your member ID (or 0 to return): ").strip()
            if member_input == "0":
                print("Returning to main menu.")
                return
            member_id = int(member_input)

            item_input = input("Enter the item ID to borrow (or 0 to return): ").strip()
            if item_input == "0":
                print("Returning to main menu.")
                return
            item_id = int(item_input)
        except ValueError:
            print("Invalid input.")
            continue
        
        with connect_db() as conn:
            cursor = conn.cursor()

            #check availability
            cursor.execute("SELECT available FROM Item WHERE itemID = ?", (item_id,))
            result = cursor.fetchone()
            if not result:
                print("Item not found.")
            elif result[0] == 0:
                print("This item is currently unavailable.")
            else:
                cursor.execute(""" 
                    INSERT INTO Loan (memberID, itemID, borrowDate, dueDate) 
                    VALUES (?, ?, DATE('now'), DATE('now','+14 days'))
                """, (member_id, item_id))
                cursor.execute("UPDATE Item SET available = 0 WHERE itemID = ?", (item_id,))
                conn.commit()
                print("Item borrowed successfully!")
        
        again = input("\nBorrow another item? (y/n): ").lower()
        if again != 'y':
            print("Returning to main menu")
            return

def return_item():
    while True:
        try:
            load_input = input("Enter loan ID (or 0 to return): ").strip()
            if load_input == "0":
                print ("Returning to main menu.")
                return
            loan_id = int(load_input)

            member_input = input("Enter your member ID: ").strip()
            member_id = int(member_input)
        except ValueError:
            print("Invalid input.")
            continue

        with connect_db() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    SELECT itemID, dueDate, returnDate FROM Loan 
                    WHERE loanID = ? AND memberID = ?
                """, (loan_id, member_id))
                loan = cursor.fetchone()

                if not loan:
                    print("Load not found or does not belong to you.")
                    continue
                elif loan[2] is not None:
                    print("Item has already been returned.")
                    continue

                item_id = loan[0]
                due_date = datetime.datetime.strptime(loan[1], "%Y-%m-%d").date()
                today = datetime.date.today()

                cursor.execute("""
                    UPDATE Loan SET returnDate = ? WHERE loanID = ?
                """,(today, loan_id))
                cursor.execute("""
                    UPDATE Item SET available = 1 WHERE itemID = ?
                """, (item_id,))

                if today > due_date:
                    fine_amount = 5
                    cursor.execute("""
                        INSERT INTO Fine (loanID, amount) VALUES (?, ?)
                    """, (loan_id, fine_amount))
                    print(f"Late return! A fine of ${fine_amount} has been applied.")

                conn.commit()
                print("Item returned successfully!")
            
            except sqlite3.Error as e:
                conn.rollback()
                print(f"Database error: {e}")
        
        again = input("\n🔁 Return another item? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("↩️ Returning to main menu.")
            return
        
def donate_item():
    while True:
        print("\nDonate Item(s) to the Library!")

        try:
            member_id = int(input("Enter your member ID (or 0 to return): ").strip())
            if member_id == 0:
                print("Returning to main menu.")
                return
            
            description = input("Describe the item(s) you wish to donate: ").strip()
            if not description:
                print("Description cannot be empty.")
                continue

            num_items = int(input("How many items are you donating? ").strip())
            if num_items <= 0:
                print("Cannot donate negative number of items.")
                continue

        except ValueError:
            print("Invalid input.")
            continue

        with connect_db() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Donation (memberID, description, status, numItems)
                    VALUES (?, ?, 'pending', ?)
                """, (member_id, description, num_items))
                conn.commit()
                print("Thank you! Your donation request has been submitted and is pending review!")
            except sqlite3.Error as e:
                conn.rollback()
                print("Database error: {e}")

        again = input("\n🔁 Donate another item? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("↩️ Returning to main menu.")
            return
        

def view_event():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Events")
        events = cursor.fetchall()

        if not events:
            print("No upcoming events.")
        else:
            print("\nUpcoming Library Events:\n")
            for event_id, name, date, time, event_type, audience in events:
               print(f"ID: {event_id} | Name: {name} | Date: {date} | Time: {time} | Type: {event_type} | Audience: {audience}")

        input("\nPress Enter to return to the main menu...")

def register_for_event():
    valid_roles = ("attendee", "host", "speaker")

    while True:
        print("\n Register for a Library Event")

        try:
            member_id = int(input("Enter your member ID (or 0 to return): ").strip())
            if member_id == 0:
                print("Returning to main menu")
                return

            event_id = int(input("Enter event ID you want to register for: ").strip())

            role = input("Enter your role (attendee, host, speaker): ").strip().lower()
            if role not in valid_roles:
                print("Invalid role. Choose from: attendee, host or speaker.")
                continue
        
        except ValueError:
            print("Invalid input.")
            continue

        with connect_db() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT fname, lname FROM Member WHERE memberID = ?", (member_id,))
                member = cursor.fetchone()
                if not member:
                    print("Member ID not found.")
                    continue

                cursor.execute("SELECT name FROM Events WHERE eventID = ?", (event_id,))
                event = cursor.fetchone()
                if not event:
                    print("Event ID not found.")
                    continue

                cursor.execute("""
                    INSERT INTO Registrations (personID, eventID, registrationDate, role)
                    VALUES (?, ?, DATE('now'), ?)
                """, (member_id, event_id, role))
                conn.commit()
                print(f"You have been registered for '{event[0]}' as a {role.title()}.")

            except sqlite3.Error as e:
                conn.rollback()
                print(f"Database error: {e}")

        again = input("\n🔁 Register for another event? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("↩️ Returning to main menu.")
            return
        
def volunteer():
    while True:
        print("\nVolunteer at the Libary")

        try:
            member_id = int(input("Enter your member ID (or 0 to return to main menu): ").strip())
            if member_id ==0:
                print("Returning to main menu.")
                return
            
            role = input("Enter the volunteer role you're applying for (bookshelver, event helper): ").strip()
            if not role:
                print("Role cannot be empty.")
                continue
        
        except ValueError:
            print("Invalid input")
            continue

        with connect_db() as conn:
            cursor = conn.cursor()
            try:
                
                cursor.execute("SELECT fname, lname FROM Member WHERE memberID = ?", (member_id,))
                member = cursor.fetchone()
                if not member:
                    print("Member ID not found.")
                    continue

                
                cursor.execute("SELECT * FROM Personnel WHERE memberID = ?", (member_id,))
                if cursor.fetchone():
                    print("This member is already volunteering or working at the library.")
                    continue

                cursor.execute("""
                    INSERT INTO Personnel (memberID, jobTitle, startDate)
                    VALUES (?, ?, DATE('now'))
                """, (member_id, role))
                conn.commit()
                print(f"{member[0]} {member[1]} is now volunteering as a '{role.title()}'.")

            except sqlite3.Error as e:
                conn.rollback()
                print(f"Database error: {e}")

        again = input("\nRegister another volunteer? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("↩️ Returning to main menu.")
            return

def ask_librarian_help():
    while True:
        print("\nAsk a Librarian for Help")

        try:
            member_id = int(input("Enter your member ID (or 0 to cancel): ").strip())
            if member_id == 0:
                print("Returning to main menu.")
                return

            issue = input("Describe your issue: ").strip()
            if not issue:
                print("Issue cannot be empty.")
                continue

        except ValueError:
            print("Invalid input. Please enter a valid member ID.")
            continue

        with connect_db() as conn:
            cursor = conn.cursor()

            try:
                # Check if the member exists
                cursor.execute("SELECT * FROM Member WHERE memberID = ?", (member_id,))
                if not cursor.fetchone():
                    print("Member ID not found.")
                    continue

                # Select a librarian from Personnel
                cursor.execute("""
                    SELECT memberID FROM Personnel
                    WHERE LOWER(jobTitle) = 'librarian'
                    LIMIT 1
                """)
                librarian = cursor.fetchone()

                if not librarian:
                    print("No librarians available right now. Try again later.")
                    return

                librarian_id = librarian[0]

                # Insert help request
                cursor.execute("""
                    INSERT INTO HelpRequest (memberID, librarianID, issue, solved)
                    VALUES (?, ?, ?, 0)
                """, (member_id, librarian_id, issue))

                conn.commit()
                print(f"Help request submitted! A librarian (ID: {librarian_id}) will assist you soon.")

            except sqlite3.Error as e:
                conn.rollback()
                print(f"Database error: {e}")

        again = input("\nSubmit another help request? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Returning to main menu.")
            return


            



def show_menu():
    while True:
        print("\n📚 Library Database Menu")
        print("1. View all items")
        print("2. Search for an item")
        print("3. Borrow an item")
        print("4. Return an item")
        print("5. Donate an item")
        print("6. View library events")
        print("7. Register for an event")
        print("8. Volunteer at the library")
        print("9. Ask for help from a librarian")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if choice == 1:
            view_items()
        elif choice == 2:
            search_items()
        elif choice == 3:
            borrow_item()
        elif choice == 4:
            return_item()
        elif choice == 5:
            donate_item()
        elif choice == 6:
            view_event()
        elif choice == 7:
            register_for_event()
        elif choice == 8:
            volunteer()
        elif choice == 9:
            ask_librarian_help()
        elif choice == 0:
            print("Goodbye!")
            break


if __name__ == "__main__":
    show_menu()