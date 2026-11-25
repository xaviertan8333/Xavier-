# ### create a list
# planets = ["mercury", "venus", "earth", "jupiter", "mars", "saturn", "neptune"]

# #retrieve a value from a list
# var1 = planets[3]
# print(var1)

# #change a value in a list
# print(planets)
# planets[4] = "elonworld"
# print(planets)

# #delete a value from a list
# #delete using index del()
# del planets[3]
# planets.pop(3)
# print(planets)

# #delete using value remove()
# planets.remove("mercury")
# print(planets)

#add a value from a lists
# planets.append("pluto")
# print(planets)


# #### loop through a list
# # ['venus', 'earth', 'jupiter', 'saturn', 'neptune']
# # for p in planets:
# #     print(p)

# for i in range(len(planets)): #0,1,2,3,4
#     print(planets[i])

## existence check
# check = input("Enter a planet: ")
# if check in planets:
#     print(f"{check} is a planet. ")
# else: 
#     print(f"{check} is not a planet. ")


prices = {"PEN":1.20,
          "FILE":2.20,
          "ERASOR":3.20,
          "PENCIL":4.20,
          "PAPER":5.20,
          "NOTEBOOK":6.20,}

# write a python function expensive_items(prices, amount)

# function must return a list containing item codes of 
# all items whose prices are greater than amount

def expensive_items(prices, amount):

    listitems = []

    for code in prices:
        money = prices[code] 
        if money > amount:
            listitems.append(code)

    return listitems

richitems = expensive_items(prices, 5)
print(richitems)