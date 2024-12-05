items = [
    {'name': 'Laptop', 'condition': 'New', 'available': True},
    {'name': 'Tablet', 'condition': 'Used', 'available': True},
    {'name': 'Scientific Calculator', 'condition': 'New', 'available': True},
    {'name': 'USB Flash Drive', 'condition': 'New', 'available': True},
    {'name': 'Power Bank', 'condition': 'Used', 'available': True},
    {'name': 'Charger', 'condition': 'New', 'available': True},
    {'name': 'Printer', 'condition': 'Used', 'available': True}
]

def list_items():
    print("\nAvailable Gadgets:")
    for idx, item in enumerate(items, start=1):
        if item['available']:
            print(f"{idx}. {item['name']} ({item['condition']})")
