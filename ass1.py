import random


# List of possible restaurant orders
orders = (
    "Cheeseburger with Fries",
    "Margherita Pizza",
    "Grilled Chicken Caesar Salad",
    "Spaghetti Bolognese",
    "California Roll",
    "Veggie Burrito",
    "BBQ Ribs with Coleslaw",
    "Chicken Parmesan",
    "Fish Tacos",
    "Mushroom Risotto"
)

pices = [
    12,  # Cheeseburger with Fries
    14,  # Margherita Pizza
    11,  # Grilled Chicken Caesar Salad
    13,  # Spaghetti Bolognese
    9,   # California Roll
    8,   # Veggie Burrito
    18,  # BBQ Ribs with Coleslaw
    16,  # Chicken Parmesan
    10,  # Fish Tacos
    15   # Mushroom Risotto
]

ord_ord = {}

orders_price = dict(zip(orders, pices))

cust_ord = []



ord_id = int((random.random()*1000000000000))
from collections import Counter
items = Counter()

fin_price = 0
name = ''

def menu():
    print("Welcome to **** restaurant")
    name = input("Can I get your name please?: ")
    seat = input("Do you want the menu or you know what to choose?\n"
                 "1. Menue\n"
                 "2. Order\n")
    if seat=='1':
        print("These are the orders")
        for i in range(len(orders)):
            print(f"{i+1}. {orders[i]} -- {pices[i]}$")
    else:
        pass
    ord = input("Enter a number separated by space for all your orders: ").split()
    cust_ord.extend(ord)
    cust_ord.sort()
    items.update(cust_ord)
    print(items)

def ords():
    count = 0
    tot_price = 0
    print()
    print("Your order is: ")
    for i in range(len(items)):
        count += 1
        key_li = list(items.keys())
        val_li = list(items.values())
        tot_price += pices[int(key_li[i])-1] * val_li[i]
        if val_li[i]>1:
            print(f"{count}. {orders[int(key_li[i])-1]} - {pices[int(key_li[i])-1]} * {val_li[i]}")
        else:
            print(f"{count}. {orders[int(key_li[i])-1]} - {pices[int(key_li[i])-1]}")

    fin_price = tot_price + tot_price*.15

    place_ord = input("Do you want to place the order or do you want to change it?\n"
                      "1. Place order\n"
                      "2. Edit\n")
    if place_ord=='1':
        print(f"Your order with a unique id of {ord_id} has been placed")
        print(f"The total is {fin_price} with 15% VAT")


menu()
ords()