# use for loop and print out numbers from 0 - 9
# for i in range(0, 10):
#     print(i)

# use for loop and print out numbers from 10 - 15
# for i in range(10, 16):
#     print(i)
# print out all the letters in the string "SINGAPORE"
# for country in "SINGAPORE":
#     print(country)
    
# use a while loop to print multiples of 3 from from 3 to 36
# number = 3
# while number < 37:
#     print(number)
#     number = number + 3

# ask a person to input a year between 1900 and 2000, 
# assume the person always enters a number
# if the person enters a wrong value, ask again
while True:
    number = int(input("Enter a year "))
    if number >= 1900 and number <= 2000:
        print("It is accepted ")
        break
    else:
        print("Your number isnt accepted ")
