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

orders_price = dict(zip(orders, pices))

cust_ord = []

def menu():
    print("Welcome to **** restaurant")
    name = input("Can I get your name please?: ")
    seat = input("Do you want the menue or you know what to choose?\n"
                 "1. Menue\n"
                 "2. Order\n")
    if seat=='1':
        print("These are the orders")
        for i in range(len(orders)):
            print(f"{i+1}. {orders[i]} -- {pices[i]}$")
    else:
        pass
    ord = input("Enter a number separated by space for all your orders: ").split()
    cust_ord = [i for i in ord]
    cust_ord.sort()
    print(cust_ord)

print("dsadsadsadsa")
print(cust_ord)
def ords():
    count = 0
    tot_price = 0
    print("fdsafdsafds")
    for i in range(len(cust_ord)):
        print("fdsasafsa")
        count += 1
        tot_price += int(pices[int(i)])
        print(f"{count}. {orders[int(cust_ord[i])]} - {pices[int(cust_ord[i])]}")
        place_ord = input("Do you want to place the order or do you want to change it?\n"
                          "1. Place order\n"
                          "2. Edit\n")
        if place_ord=='1':
            print(f"Your order with a unique id of {(random.random()*100000000)%10000000}")
            print(f"The total is {tot_price+tot_price*.15} with 15% VAT")


menu()
ords()
