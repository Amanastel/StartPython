import random

def main():
    print("Welcome to Zomato Chronicles: The Great Food Fiasco!")

    menu = {
        1: {
            "name": "Pizza",
            "price": 12.99,
            "availability": True
        },
        2: {
            "name": "Burger",
            "price": 8.99,
            "availability": False
        },
        # Add more dishes to the menu.
    }
    count = len(menu)  # Initialize count with the current number of dishes
    orders = []

    while True:
        print("\nMenu:")
        for dish_id, dish_info in menu.items():
            availability_status = "Available" if dish_info['availability'] else "Not Available"
            print(f"{dish_id}. {dish_info['name']} - ${dish_info['price']:.2f} ({availability_status})")

        print("\nChoices:")
        print("1. Add a new dish")
        print("2. Remove a dish")
        print("3. Update dish availability")
        print("4. Take a new Order")
        print("5. Review All orders")
        print("6. Update the status of an order")
        print("7. Filter orders by status")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            count += 1
            dish_id = count
            name = input("Enter the dish name: ")
            price = float(input("Enter the dish price: "))
            availability = input("Is the dish available? (yes/no): ").lower() == 'yes'

            menu[dish_id] = {
                "name": name,
                "price": price,
                "availability": availability
            }

        elif choice == '2':
            dish_id = int(input("Enter the dish ID to remove: "))
            if dish_id in menu:
                del menu[dish_id]
                print("Dish removed successfully!")
            else:
                print("Invalid dish ID. The dish does not exist in the menu.")

        elif choice == '3':
            dish_id = int(input("Enter the dish ID to update availability: "))
            if dish_id in menu:
                availability = input("Is the dish available now? (yes/no): ").lower() == 'yes'
                menu[dish_id]['availability'] = availability
                print("Dish availability updated successfully!")
            else:
                print("Invalid dish ID. The dish does not exist in the menu.")

        elif choice == '4':
            customer_name = input("Enter the customer's name: ")
            order_dish_ids = [int(x) for x in input("Enter dish IDs (comma-separated) the customer wants to order: ").split(',')]

            # Check if all dishes in the order are available
            order_available = all(menu.get(dish_id, {}).get('availability', False) for dish_id in order_dish_ids)

            if order_available:
                # Process the order and assign a unique order ID
                order_id = generate_unique_order_id()
                print(f"Order for {customer_name} received. Order ID: {order_id}")

                # Update the order status as 'received'
                orders.append({
                    "order_id": order_id,
                    "customer_name": customer_name,
                    "dish_ids": order_dish_ids,
                    "status": "received"
                })
            else:
                print("Sorry, some dishes in the order are not available. Cannot process the order.")

        elif choice == '5':
            if not orders:
                print("No orders yet. The kitchen is waiting for the first culinary adventure!")
            else:
                print("\nAll Orders:")
                for order in orders:
                    print_order_details(order)

        elif choice == '6':
            order_id_to_update = int(input("Enter the order ID to update status: "))

            # Find the order in the 'orders' list based on the order ID
            order_found = False
            for order in orders:
                if order['order_id'] == order_id_to_update:
                    order_found = True
                    new_status = input("Enter the new status (preparing/ready for pickup/delivered): ").lower()
                    order['status'] = new_status
                    print(f"Order ID {order_id_to_update} status updated to '{new_status}'.")
                    break

            if not order_found:
                print("Invalid order ID. The order does not exist.")

        elif choice == '7':
            print("Filter orders by status:")
            filter_status = input("Enter the status (preparing/ready for pickup/delivered): ").lower()
            print_filtered_orders(orders, filter_status)

        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break

# ... (unchanged)

def print_order_details(order):
    print(f"Order ID: {order['order_id']}")
    print(f"Customer Name: {order['customer_name']}")
    print(f"Dish IDs: {', '.join(map(str, order['dish_ids']))}")
    print(f"Status: {order['status']}\n")

def print_filtered_orders(orders, status):
    filtered_orders = [order for order in orders if order['status'] == status]
    if not filtered_orders:
        print("No orders found with the specified status.")
    else:
        print("\nFiltered Orders:")
        for order in filtered_orders:
            print_order_details(order)

if __name__ == "__main__":
    main()
