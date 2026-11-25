capital_cities = {
    'singapore':'Singapore',
    'japan':'Tokyo', 
    'australia':'Canberra',
    'england':'London',
    'france':'Paris',
    'germany':'Berlin'
}

# For all sub-tasks, you can assume that all user input is valid. 
# All countries input to be searched or removed are found in the dictionary.

#=================================================================
# Task 3.1
# Ask the user to input a country
# • converts the input for country to lower case
# • searches the dictionary for the country input and outputs 
#    the capital city of that country.
# Save your program.    [3]

country = input("Name a country: ")

country = country.lower()

if country in capital_cities:
    print(f"The capital of {country} is {capital_cities[country]}")

else:
    print(f"{country} doesnt exist")



#=================================================================
# Task 3.2
# Copy and paste your program from sub-task 3.1.
# Edit the program so that if the user enters the value ‘Y’ for remove, the program:
# • allows the user to input a country they want to remove from the dictionary
# • converts the country input to lower case
# • removes the country from the dictionary that is input by the user.
# Save your program.   [3]

remove = input("Would you like to remove any of the entries? (Y or N): ")

if remove == "Y":
    county_remove = input("Which country do you want to remove? ").lower()
    del capital_cities[county_remove]
    print(capital_cities)



#=================================================================
# Task 3.3
# Copy and paste your program from sub-task 3.2 .
# Edit the program so that if the user enters the value ‘Y’ for add, the program:
# • allows the user to input a country they want to add to the diction nary
# • allows the user to input the capital city for the country they want to add
# • adds the country and its capital city to the dictionary in the format country:capital
# • outputs the dictionary at the end of the program.
# Save your JupyterLab notebook for Task 3.      
#=================================================================
add = input("Would you like to add a new entry? (Y or N): ")
if add == "Y":
    country_add = input("What country do you want to add? ")
    country_capital = input("What is the capital? ")

    capital_cities[country_add] = country_capital

print(capital_cities)
                       
