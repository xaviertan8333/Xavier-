# ctrl-c > copy
# ctrl-x > cut
# ctrl-v > paste
# ctrl-z > undo
# ctrl-a > select all
# ctrl-? > comment/ uncomment
# ctrl ] > indent right
# ctrl [ > indent left

# Task 1
# Open the file EIGHT .i pynb Save the file as: TASK2 .i pynb'
# The task is to edit program code that allows the user to enter and edit the names and heights of
# team members

#--------------------------------------------------------
# Task 1.1 [4]
# The following program allows the user to enter the names of the 5 members of a team and
# stores them in a list. The list is to be sorted and processed in each sub-task.
# # This program allows the user to enter five names and
# stores the names in a list for further processing

# variables
names = []
# Enter name
for i in range(5) :
    name = input ('Please enter the name:')
    names.append(name )

# Processing
print (names)

# Edit the program so that it:
# (a) creates a new list to store the collection of height data for the corresponding names
# input.
# (b) allows the user to enter height data.
# (c) identifies the tallest and shortest height (not the person) among the entered data.
# Save your program.
#--------------------------------------------------------

# height = []
# # for h in range(5):
# #     heights = int(input("What is your height, assuming that it is in cm "))
# #     height.append(heights)

# for h in names:
#     heights = int(input(f"Enter the height for {h} (in cm): "))
#     height.append(heights)

# tallest = max(height)
# shortest = min(height)

# # print(f"The shortest height is {shortest} cm, and the tallest height is {tallest} cm ")


# #--------------------------------------------------------
# # Task 1.2 [3]
# # Copy and paste your program from sub-task 1.1.
# # Edit the program to perform presence check and type check data validation on the input for
# # height data.
# # Save your program.
# #--------------------------------------------------------

# height = []
# # for h in range(5):
# #     heights = int(input("What is your height, assuming that it is in cm "))
# #     height.append(heights)


# for h in names:
#     while True:
#         heights = input(f"Enter the height for {h} (in cm): ")
#         if heights == "":
#             print("You must type a value")
#         elif not heights.isdigit():
#             print("Type a number.")
#         else:
#             print("Success")
#             break
#     height.append(heights)

# tallest = max(height)
# shortest = min(height)

# print(f"The shortest height is {shortest} cm, and the tallest height is {tallest} cm ")




#--------------------------------------------------------
# Task 1.3 [4]
# Copy and paste your program from sub-task 1.
# Edit the program so that it prints out:
# (a) the tallest and the shortest person from the entered data.
# (b) the average of the heights of the entered data.
# (c) the range of the heights data.
# Save your JupyterLab notebook for Task 1.
#--------------------------------------------------------
height = []

for h in names:
    while True:
        heights = input(f"Enter the height for {h} (in cm): ")
        if heights == "":
            print("You must type a value")
        elif not heights.isdigit():
            print("Type a number.")
        else:
            print("Success")
            break
    height.append(int(heights))

tallest = max(height)
shortest = min(height)

print(f"The shortest height is {shortest} cm, and the tallest height is {tallest} cm ")

#### Task 1.3
pos_tall = height.index(tallest)
tallest_person = names[pos_tall]
print(f"The tallest person is {tallest_person}")

pos_short = height.index(shortest)
shortest_person = names[pos_short]
print(f"The shortest person is {shortest_person}")

total_height = sum(height)
num_height = len(height)
average_height = total_height/num_height
print(f"The average height is {average_height}.")

print(f"The range for height is {shortest} to {tallest}")