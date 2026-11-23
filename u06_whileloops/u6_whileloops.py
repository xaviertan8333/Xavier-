# for loop and while loop

# print numbers from 10 to 20

# count = 10
# while count < 21:
#     print(count)
#     count = count + 1

# print multiples of 3 from 3 to 36
# count = 3
# while count < 37:
#     print(count)
#     count = count + 3


# write a program to ask a person for their age
# validate that the input is a number
# one 

# while True:
#     age = input("What is your age? ")
#     if age.isdigit():
#         print("Your age is accepted. ")
#         break
#     else:
#         print("Enter your age in numbers again. ")

# ask for a first name
# validate that it must be letters
# while True: 
#     name = input("What is your name? ")
#     if name.isalpha():
#         print("Your name is accepted. ")
#         break
#     else:
#         print("Enter your name is letters again. ")

####
# generate 2 random numbers between 10 and 30
# ask the student "What is 13 + 23? "
# if the student answer wrongly, keep asking again and again

import random

for i in range(10):
    rannum1 = random.randint(10,30)
    rannum2 = random.randint(10,30)

    while True:
        answer = input(f"What is {rannum1} + {rannum2}? ")
        if int(answer) == rannum1 + rannum2: #39 == "39"
            print("Your answer is correct! ")
            break
        else:
            print("Try Again. ")



