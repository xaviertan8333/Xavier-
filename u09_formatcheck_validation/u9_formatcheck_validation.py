# var1 = "SINGAPORE"

# # var2 = var1.upper()
# # print(var2) 

# # var3 = var1.isupper() # True or False
# # print(var3)

# # print("Z" in var1)

# height, check for presence, as well as check for integers

while True:
    height = input("What is your height? ")
    if height == "":
        print("Type a number")
    elif not height.isdigit():
        print("Type a number")
    else:
        print("Success")
        break