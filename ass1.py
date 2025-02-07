import random
from collections import Counter

# Menu stored as tuples with item name and price
menu = (
    ("Cheeseburger with Fries", 12),
    ("Margherita Pizza", 14),
    ("Grilled Chicken Caesar Salad", 11),
    ("Spaghetti Bolognese", 13),
    ("California Roll", 9),
    ("Veggie Burrito", 8),
    ("BBQ Ribs with Coleslaw", 18),
    ("Chicken Parmesan", 16),
    ("Fish Tacos", 10),
    ("Mushroom Risotto", 15)
)

# Files to store orders and unique customers
orders_file = "orders.txt"
customers_file = "customers.txt"

def waits():
    input("Press Enter to continue...")

def show_menu():
    print("Menu:")
    for idx in range(len(menu)):
        print(f"{idx + 1}. {menu[idx][0]} - ${menu[idx][1]}")

def save_order(order_id, name, items, total_price):
    with open(orders_file, "a") as file:
        file.write(f"{order_id},{name},{'|'.join(items)},{total_price}\n")
    save_customer(name)

def save_customer(name):
    customers = load_customers()
    if name not in customers:
        with open(customers_file, "a") as file:
            file.write(f"{name}\n")

def load_orders():
    orders = []
    try:
        with open(orders_file, "r") as file:
            for line in file:
                order_id, name, items, total_price = line.strip().split(",")
                orders.append((int(order_id), name, items.split("|"), float(total_price)))
    except FileNotFoundError:
        pass
    return orders

def load_customers():
    customers = set()
    try:
        with open(customers_file, "r") as file:
            for line in file:
                customers.add(line.strip())
    except FileNotFoundError:
        pass
    return customers

def place_order():
    name = input("Enter your name: ")
    show_menu()
    order_numbers = input("Enter item numbers separated by spaces: ").split()
    selected_items = []
    total_price = 0
    for i in order_numbers:
        if i.isdigit() and 1 <= int(i) <= len(menu):
            selected_items.append(menu[int(i) - 1][0])
            total_price += menu[int(i) - 1][1]
    order_id = random.randint(100000, 999999)
    save_order(order_id, name, selected_items, total_price)
    print(f"Order placed! Your order ID is {order_id}")
    waits()

def find_order():
    order_id = input("Enter your order ID to search: ")
    orders = load_orders()
    for order in orders:
        if str(order[0]) == order_id:
            item_counts = Counter(order[2])
            print("\n--- Order Found ---")
            print(f"Order ID   : {order[0]}")
            print(f"Customer   : {order[1]}")
            print("Items      :")
            for item, count in item_counts.items():
                print(f"  - {item} {'* ' + str(count) if count > 1 else ''}")
            print(f"Total Price: ${order[3]:.2f}\n")
            waits()
            return
    print("Order not found!")
    waits()

def remove_order():
    order_id = input("Enter your order ID to cancel: ")
    orders = load_orders()
    updated_orders = [order for order in orders if str(order[0]) != order_id]
    with open(orders_file, "w") as file:
        for order in updated_orders:
            file.write(f"{order[0]},{order[1]},{'|'.join(order[2])},{order[3]}\n")
    print("Order canceled!")
    waits()

def generate_summary():
    orders = load_orders()
    customers = load_customers()
    total_revenue = sum(order[3] for order in orders)
    item_count = Counter()
    for order in orders:
        for item in order[2]:
            item_count[item] += 1
    top_item = item_count.most_common(1)[0] if item_count else ("None", 0)
    sorted_orders = sorted(orders, key=lambda x: x[3], reverse=True)
    print("\n--- REPORT ---")
    print(f"Total Revenue: ${total_revenue}")
    print(f"Total Unique Customers: {len(customers)}")
    print(f"Most Ordered Item: {top_item[0]} ({top_item[1]} times)")
    print("Orders sorted by price:")
    for order in sorted_orders:
        print(f"Order ID: {order[0]}, Total Price: ${order[3]}")
    waits()

def main():
    while True:
        print("\nOrder Management System")
        print("1. Place Order")
        print("2. Find Order")
        print("3. Cancel Order")
        print("4. Generate Report")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            place_order()
        elif choice == "2":
            find_order()
        elif choice == "3":
            remove_order()
        elif choice == "4":
            generate_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

#https://chatgpt.com/share/67a6013a-64c0-8003-bdcf-24b5e22ece77