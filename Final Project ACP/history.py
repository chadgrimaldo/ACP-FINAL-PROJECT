borrowed_items = []

def view_borrow_history():
    email = input("Enter your email to view history: ").strip().lower()
    history = [record for record in borrowed_items if record['user_email'] == email]
    if history:
        print("\nBorrowing History:")
        for record in history:
            status = "Returned" if record['returned'] else "Borrowed"
            print(f"{record['item_name']} - {status}")
            print(f"  Borrowed On: {record['borrow_date'].strftime('%Y-%m-%d')}")
            print(f"  Return By: {record['return_date'].strftime('%Y-%m-%d')}")
    else:
        print("No borrowing history found.")
