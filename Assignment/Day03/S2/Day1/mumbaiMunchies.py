
class CanteenApp:
    def __init__(self):
        self.inventory = []
        self.sales_records = []

    def add_snack(self, snack_id, name, price):
        snack = {'id': snack_id, 'name': name, 'price': price, 'available': True}
        self.inventory.append(snack)

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack['id'] == snack_id:
                self.inventory.remove(snack)
                break
            

    def update_availability(self, snack_id, available):
        for snack in self.inventory:
            if snack['id'] == snack_id:
                snack['available'] = available
                break

    def record_sale(self, snack_id):
        for snack in self.inventory:
            if snack['id'] == snack_id and snack['available']:
                sale_item = snack.copy()  # Create a copy of the snack
                sale_item['available'] = False  # Set the availability of the copied snack
                self.sales_records.append(sale_item)  # Append the copied snack to sales_records
                snack['available'] = False  # Update the original snack's availability
                break
        else:
            print("Snack not found or unavailable.")

    def display_inventory(self):
        for snack in self.inventory:
            print(f"ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}, Available: {'Yes' if snack['available'] else 'No'}")

    def display_sales_records(self):
        for snack in self.sales_records:
            print(f"ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}, Available: {'Yes' if snack['available'] else 'No'}")

app = CanteenApp()

while True:
    print("\n1. Add Snack\n2. Remove Snack\n3. Update Availability\n4. Record Sale\n5. Display Inventory\n6. Display Sales Records\n7. Quit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        snack_id = int(input("Enter Snack ID: "))
        name = input("Enter Snack Name: ")
        price = float(input("Enter Snack Price: "))
        app.add_snack(snack_id, name, price)
    elif choice == 2:
        snack_id = int(input("Enter Snack ID to remove: "))
        app.remove_snack(snack_id)
    elif choice == 3:
        snack_id = int(input("Enter Snack ID to update: "))
        available = input("Is snack available? (yes/no): ").lower() == 'yes'
        app.update_availability(snack_id, available)
    elif choice == 4:
        snack_id = int(input("Enter Snack ID sold: "))
        app.record_sale(snack_id)
    elif choice == 5:
        app.display_inventory()
    elif choice == 6:
        app.display_sales_records()
    elif choice == 7:
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
