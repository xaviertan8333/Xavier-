# range(stop) range(10)
### print out the numbers from 0 to 9
# for i in range(16):
#     print(i)

# range(start, stop)
### print out from 5 to 25
# for i in range(5, 26):
#     print(i)

# range(start, stop, step)
# print numbers from 2 to 20, in multiples of 2
# for i in range(2, 21, 2):
#     print(i)

# print out multiples of 7 from 7 to 70
# for i in range(7, 71, 7):
#     print(i)

# write out a times table program
# ask for a number e.g. 7
# print out the timestable for that number up till 12 times
# 7 x 1 = 7
# 7 x 2 = 14
#....
# number = int(input("Give me a number: ")) #int
# for i in range(1 , 13):
#     print(f"{number} x {i} = {number*i}")   

    # 7 x 1 = 7

#### Format string
# name = "John"
# age = 14
# hobby = "swim"

# # print(name, "is",age,"and he likes to",hobby) # ONLY WORKS IN A PRINT
# # print(name + " is "+ str(age) + " and he likes to " + hobby)
# # print("{} is {} and he likes to {}".format(name, age, hobby)) # EXAM APPROVED WAY
# print(f"{name} is {age} and he likes to {hobby}")

# # you are a citizen of a country 
# # I live in SIngapore, it is 61 years old and has a population of 8000000
# country = "Singapore"
# country_age = 61
# population = 8000000
# print(f"i live in {country}, it is {country_age} years old and has a population of {population}")


# for i in range(3):
#     print("baa")

# for j in range(3):
#     print("waa")


#### do a cheer
name = "XAVIER"

# "Give me a X!"
# "Give me a A!"
# "Give me a V!"
# "Give me a I!"
# "Give me a E!"
# "Give me a R!"
# WHO IS THE BEST???!
# XAVIER!

for char in name:
    print(f"Give me a {char}!" )

print("WHO IS THE BEST???!")
print(f"{name}!")

print(f"{name} has {len(name)} characters")