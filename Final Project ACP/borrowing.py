import datetime
from items import items
from utils import get_valid_number
from history import borrowed_items

def select_duration():
    durations = {1: 1, 2: 2, 3: 3, 7: 7, 30: 30}
    print("\nSelect borrowing duration:")
    for idx, days in enumerate(durations.values(), start=1):
        print(f"{idx}. {days} days")
    while True:
        try:
            choice = int(input("Enter duration number: "))
            if 1 <= choice <= len(durations):
                return list(durations.values())[choice - 1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def borrow_item():
    from items import list_items 
    list_items()
    try:
        choice = int(input("Select gadget number to borrow: ")) - 1
        if 0 <= choice < len(items) and items[choice]['available']:
            duration = select_duration()
            print(f"\nNote: If you return the gadget late, the penalty is ₱50 per day, up to a maximum of ₱1000.")
            confirm = input("Do you want to proceed? (yes/no): ").strip().lower()

            if confirm == 'yes':
                borrow_record = {
                    'user_email': input("Enter your email: "),
                    'item_name': items[choice]['name'],
                    'borrow_date': datetime.datetime.now(),
                    'return_date': datetime.datetime.now() + datetime.timedelta(days=duration),
                    'returned': False,
                    'duration': duration,
                    'penalty': 0
                }
                borrowed_items.append(borrow_record)
                items[choice]['available'] = False
                print(f"\n{items[choice]['name']} borrowed successfully!")
            else:
                print("Borrowing cancelled.")
        else:
            print("Invalid choice or item not available.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def return_item():
    email = input("Enter your email: ")
    borrowed_records = [record for record in borrowed_items if record['user_email'] == email and not record['returned']]
    if not borrowed_records:
        print("No items to return.")
        return

    for idx, record in enumerate(borrowed_records, start=1):
        print(f"{idx}. {record['item_name']} - Due on {record['return_date'].strftime('%Y-%m-%d')}")
    try:
        choice = int(input("Select the item number to return: ")) - 1
        if 0 <= choice < len(borrowed_records):
            returned_item = borrowed_records[choice]
            returned_item['returned'] = True
            overdue_days = (datetime.datetime.now() - returned_item['return_date']).days
            penalty = min(overdue_days * 50, 1000) if overdue_days > 0 else 0
            returned_item['penalty'] = penalty
            for item in items:
                if item['name'] == returned_item['item_name']:
                    item['available'] = True
                    break
            print(f"{returned_item['item_name']} returned successfully! Penalty: ₱{penalty}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")
