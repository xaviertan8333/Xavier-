# create a dictionary variable
menu = {"pizza":23.50, "hamburger":8.69, "fries":4.90, "cola":3.99}

#retrieving a value from a dictionary
var1 = menu["fries"]
print(var1)

# how to change a value for a key
menu["hamburger"] = 10.99
print(menu)

# add a new key and value pair into dictionary
menu["soup"] = 12.50
print(menu) 

# delete key value pair from dictionary
del menu["cola"]
print(menu)

# loop through a dictionary
# for item in menu:
    # print(item)
    # print(menu[item])

    # print(f"{item} costs ${menu[item]}")

for food, price in menu.items():
    print(f"{food} costs ${price}")

order = "pasta"

if order in menu:
    print(f"{order} costs ${menu[order]}")
else:
    print(f"Sorry i do not sell {order}")


