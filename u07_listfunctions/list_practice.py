#### create a list of planets
planets = ["Mars", "Mercury", "Neptune", "Saturn"]

# # retrieve a value from a list
planet = planets[1] 
print(planet)

# # change a value in the list
planets[3] = "Earth"
print(planets)

# # delete a value from a list del
del planets[0]
print(planets)

# # delete using value remove()
planets.remove("Neptune")
print(planets)
# add a value into the list
planets.append("Pluto")
print(planets)

#### loop through all the values in the list
for p in planets:
    print(p)

## check if a value exists in the list 
if "Earth" in planets:
    print("It exists")
else:
    print("it doesnt exist")