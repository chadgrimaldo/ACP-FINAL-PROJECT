from registration import register_user
from items import list_items
from borrowing import borrow_item, return_item
from history import view_borrow_history

def main_menu():
    while True:
        print("\n===== SmartShare Menu =====")
        print("1. Registration")
        print("2. List of Available Gadgets")
        print("3. Borrow a Gadget")
        print("4. View Borrowing History")
        print("5. Return a Gadget")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            list_items()
        elif choice == '3':
            borrow_item()
        elif choice == '4':
            view_borrow_history()
        elif choice == '5':
            return_item()
        elif choice == '6':
            print("Thank you for using SmartShare!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main_menu()
