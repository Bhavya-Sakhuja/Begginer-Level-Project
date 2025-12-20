menu = {
    'Pizza': 40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80
}

print("Welcome to our restraunt. Here's the menu:")
print("Pizza: Rs40 \nPasta: Rs50 \nBurger: Rs60 \nSalad: Rs70 \nCoffee: Rs80")

order = input('Enter your first item you want to Order = ').capitalize()

items = [] 

if order in menu:
  items.append(order)
  print(f"Order of {order} has been added.")

else:
    print("item not found")

more_item = input('Do you want anything else? ')

while(more_item == 'yes'):
    order = input('Enter item you want to Order = ').capitalize()
    items.append(order) 
    if order in menu:
      print(f"Order of {order} has been added.")
    else:
       print("item not found")

    total = 0
    
    for ordered_items in items:
        total += menu[ordered_items]    

    print(f"The total price to pay is: {total}")

    more_item = input('Do you want anything else? ')

    