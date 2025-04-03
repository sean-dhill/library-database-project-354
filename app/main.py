import sqlite3
import datetime

DB_PATH = "database/library.db"

def connect_db():
    return sqlite3.connect(DB_PATH)

def view_items():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Items")
        items = cursor.fetchall()
        print("\n📚 All Library Items:")
        for item in items:
            item_id, name, item_type, fmt, available, date_added, price = item
            status = "Yes" if available else "No"
            print(f"ID: {item_id} | Title: {name} | Type: {item_type} | Format: {fmt} | Available: {status} | Date Added: {date_added} | Price: ${price}")
        input("\nPress Enter to return to main menu...")

def search_items():
    while True:
        keyword = input("🔍 Enter keyword to search (or 0 to return): ").strip()
        if keyword == "0":
            return
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Items WHERE name LIKE ?", ('%' + keyword + '%',))
            results = cursor.fetchall()
            if results:
                for item in results:
                    item_id, name, item_type, fmt, available, date_added, price = item
                    status = "Yes" if available else "No"
                    print(f"ID: {item_id} | Title: {name} | Type: {item_type} | Format: {fmt} | Available: {status} | Date Added: {date_added} | Price: ${price}")
            else:
                print("No matching items found.")
        again = input("🔁 Search again? (y/n): ").lower()
        if again != "y":
            break

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
            print("❌ Invalid input.")
            continue

        with connect_db() as conn:
            cursor = conn.cursor()

            try:
                cursor.execute("SELECT 1 FROM Members WHERE memberID = ?", (member_id,))
                if not cursor.fetchone():
                    print("❌ Member not found.")
                    continue

                cursor.execute("SELECT available FROM Items WHERE itemID = ?", (item_id,))
                result = cursor.fetchone()
                if not result:
                    print("❌ Item not found.")
                    continue
                elif result[0] == 0:
                    print("⚠️ This item is currently unavailable.")
                    continue

                cursor.execute("SELECT COALESCE(MAX(loanID), 0) + 1 FROM Loans")
                next_loan_id = cursor.fetchone()[0]

                cursor.execute(""" 
                    INSERT INTO Loans (loanID, memberID, itemID, borrowDate, dueDate) 
                    VALUES (?, ?, ?, DATE('now'), DATE('now','+14 days'))
                """, (next_loan_id, member_id, item_id))
                cursor.execute("UPDATE Items SET available = 0 WHERE itemID = ?", (item_id,))
                conn.commit()

                due_date = datetime.date.today() + datetime.timedelta(days=14)
                print(f"✅ Item borrowed successfully! Loan ID: {next_loan_id}, Due on: {due_date}")

            except sqlite3.Error as e:
                conn.rollback()
                print(f"❌ Database error: {e}")

        again = input("\n🔁 Borrow another item? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("↩️ Returning to main menu.")
            return

def return_item():
    while True:
        try:
            loan_id = int(input("Enter loan ID (or 0 to return): "))
            if loan_id == 0:
                return
            member_id = int(input("Enter your member ID: "))
        except ValueError:
            print("❌ Invalid input.")
            continue
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT itemID, dueDate, returnDate FROM Loans
                WHERE loanID = ? AND memberID = ?
            """, (loan_id, member_id))
            loan = cursor.fetchone()
            if not loan:
                print("❌ Loan not found.")
                continue
            if loan[2] is not None:
                print("⚠️ This item was already returned.")
                continue

            item_id = loan[0]
            due_date = datetime.datetime.strptime(loan[1], "%Y-%m-%d").date()
            today = datetime.date.today()

            cursor.execute("UPDATE Loans SET returnDate = ? WHERE loanID = ?", (today, loan_id))
            cursor.execute("UPDATE Items SET available = 1 WHERE itemID = ?", (item_id,))

            if today > due_date:
                cursor.execute("SELECT 1 FROM Fines WHERE loanID = ?", (loan_id,))
                if not cursor.fetchone():
                    cursor.execute("INSERT INTO Fines (loanID, amount) VALUES (?, ?)", (loan_id, 5))
                    print("⚠️ Late return! $5 fine applied.")
            conn.commit()
            print("✅ Return successful.")
        again = input("🔁 Return another item? (y/n): ").lower()
        if again != "y":
            break

def donate_item():
    while True:
        print("\n🎁 Donate Item(s) to the Library!")

        try:
            member_id = int(input("Enter your member ID (or 0 to return): ").strip())
            if member_id == 0:
                print("↩️ Returning to main menu.")
                return
            
            # Verify member exists
            with connect_db() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM Members WHERE memberID = ?", (member_id,))
                if not cursor.fetchone():
                    print("❌ Member ID not found.")
                    continue

            description = input("📦 Describe the item(s) you wish to donate: ").strip()
            if not description:
                print("❌ Description cannot be empty.")
                continue

            num_items = int(input("📦 How many items are you donating? ").strip())
            if num_items <= 0:
                print("❌ Number of items must be greater than zero.")
                continue

        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.")
            continue

        with connect_db() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT COALESCE(MAX(donationID), 0) + 1 FROM Donations")
                next_donation_id = cursor.fetchone()[0]

                cursor.execute("""
                    INSERT INTO Donations (donationID, memberID, description, status, numItems)
                    VALUES (?, ?, ?, 'pending', ?)
                """, (next_donation_id, member_id, description, num_items))
                
                conn.commit()
                print(f"✅ Thank you! Donation ID {next_donation_id} has been submitted and is pending review.")

            except sqlite3.Error as e:
                conn.rollback()
                print(f"❌ Database error: {e}")

        again = input("\n🔁 Donate another item? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("↩️ Returning to main menu.")
            return


def view_event():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.eventID, e.name, e.date, e.time, e.type, e.targetAudience, r.name
            FROM Events e JOIN Rooms r ON e.roomID = r.roomID
        """)
        events = cursor.fetchall()
        if not events:
            print("No upcoming events.")
        else:
            for event_id, name, date, time, event_type, audience, room in events:
                print(f"ID: {event_id} | Name: {name} | Room: {room} | Date: {date} | Time: {time} | Type: {event_type} | Audience: {audience}")
        input("\nPress Enter to return to menu...")

def register_for_event():
    while True:
        try:
            member_id = int(input("Enter your member ID (or 0 to cancel): "))
            if member_id == 0:
                return
            event_id = int(input("Enter event ID to register for: "))

            with connect_db() as conn:
                cursor = conn.cursor()

                # validate member and event
                cursor.execute("SELECT 1 FROM Members WHERE memberID = ?", (member_id,))
                if not cursor.fetchone():
                    print("❌ Member not found.")
                    continue
                cursor.execute("SELECT r.capacity FROM Events e JOIN Rooms r ON e.roomID = r.roomID WHERE e.eventID = ?", (event_id,))
                capacity_info = cursor.fetchone()
                if not capacity_info:
                    print("❌ Event not found.")
                    continue
                capacity = capacity_info[0]

                cursor.execute("SELECT COUNT(*) FROM Registers WHERE eventID = ?", (event_id,))
                current = cursor.fetchone()[0]
                if current >= capacity:
                    print("⚠️ This event is full!")
                    continue

                cursor.execute("INSERT INTO Registers (eventID, memberID) VALUES (?, ?)", (event_id, member_id))
                conn.commit()
                print("✅ Registered successfully!")
        except sqlite3.IntegrityError:
            print("⚠️ You are already registered for this event.")
        except ValueError:
            print("❌ Invalid input.")
        again = input("🔁 Register for another? (y/n): ").lower()
        if again != "y":
            break

def volunteer():
    while True:
        try:
            member_id = int(input("Enter your member ID (or 0 to cancel): "))
            if member_id == 0:
                return
            role = input("Enter volunteer role (e.g., bookshelver): ").strip()
            if not role:
                print("❌ Role cannot be empty.")
                continue
        except ValueError:
            print("❌ Invalid input.")
            continue

        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM Members WHERE memberID = ?", (member_id,))
            if not cursor.fetchone():
                print("❌ Member not found.")
                continue
            cursor.execute("SELECT 1 FROM Personnel WHERE memberID = ?", (member_id,))
            if cursor.fetchone():
                print("⚠️ Already volunteering or staff.")
                continue
            cursor.execute("INSERT INTO Personnel (memberID, jobTitle, startDate) VALUES (?, ?, DATE('now'))", (member_id, role))
            conn.commit()
            print("✅ Volunteer registered!")
        again = input("🔁 Add another volunteer? (y/n): ").lower()
        if again != "y":
            break

def ask_librarian_help():
    while True:
        try:
            member_id = int(input("Enter your member ID (or 0 to cancel): "))
            if member_id == 0:
                return
            issue = input("Describe your issue: ").strip()
            if not issue:
                print("❌ Description required.")
                continue
        except ValueError:
            print("❌ Invalid input.")
            continue
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM Members WHERE memberID = ?", (member_id,))
            if not cursor.fetchone():
                print("❌ Member not found.")
                continue
            cursor.execute("""
                INSERT INTO HelpRequests (requesterID, issue, solved)
                VALUES (?, ?, 0)
            """, (member_id, issue))
            conn.commit()
            print("✅ Help request submitted.")
        again = input("🔁 Submit another? (y/n): ").lower()
        if again != "y":
            break

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
            print("Please enter a number.")
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
