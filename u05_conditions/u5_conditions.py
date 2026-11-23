### write a program to ask the user to input a password
# if the user types correct, print "access granted" else "access denied"

# password = "pass123"
# user_pw = input("what is your password? ")
# if user_pw == password:
#     print("Access Granted")
# else:
#     print("Password Denied")

# generate a random number between 100 and 999

# rannum = random.randint(100, 999)
# print(rannum)

# generate a random number between 1 and 100

# import random
# rannum = random.randint(1, 100)
# print(rannum)




# random number guessing game

# generate a random number from 1 to 100 >>> random.randint()

# ask for a number >>> input() # number

# compare the guess vs the real number # if else

# give 7 chances >>> for loop

# import random
# rannum = random.randint(1, 100)
# print(rannum)

# for i in range(7):
#     number = int(input("What is your guess? ")) ### this must be a number, and must between 1 and 100
#     if number > rannum:
#         print("Your guess is too high")
#     elif number < rannum: 
#         print("Your guess is too low")
#     else:
#         print("You got the number")
#         break
# else:
#     ## code here will run on successful completion of the loop
#     print(f"The correct number was {rannum}")

# # if rannum != number:
    # print(f"The correct number was {rannum}")

# length check, 



pens = int(input("How many pens do you want to buy? "))
if pens >= 100:
    bulk_total = pens*5*0.9
    print(f"The total costs of the pens is ${bulk_total}")
else:
    total = pens*5
    print(f"The total costs of the pens is ${total}")

