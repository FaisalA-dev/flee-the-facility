inventory = []

def add_item(item):
    inventory.append(item)
    print(f"You have added {item} to your inventory.")

def show_inventory():
    print("Inventory:")
   
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print(f"- {item}")
