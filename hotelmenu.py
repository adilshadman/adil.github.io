menu={'Pizza':50,
      'Pasta':40,
      'Burger':60,
      'Salad':70,
      'Coffee':80
      }
print("WELCOME TO PYTHON RESTAURANT")
print('Pizza:Rs50\nPasta:Rs40\nBurger:Rs60\nSalad:Rs70\nCoffee:Rs80')

order_total=0

item_1=input("Enter the name of the item you want to order=").capitalize()

if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available yet!")

another_order=input("Do you want to order another item? (Yes/No)\n").capitalize()
if another_order=="Yes":
    item_2=input("Enter the name of the second item you want to order=").capitalize()
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"your second item {item_2} has been added to your order")
    else:
        print(f"ordered item {item_2} is not available!")

print(f"The total amount of items is {order_total}")










    
