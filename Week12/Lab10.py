# Lab 10
# Author: Bodhi Fox

# Lab 10 will show demonstrate how Dictionary's work in Python.

# 1. Create a dictionary called my_dict with the following key value pairs:
# Key: "name", Value: "John"
# Key: "age", Value: 30
# Key: "city", Value: "Trenton"
# Key: "state", Value: "New Jersey"

my_dict= {"name": "John", "age": 30, "city": "Trenton", "state": "New Jersey"}

# 2. Print out the dictionary.

print(my_dict)

# 3. Print out the value for the key "name".

print(my_dict["name"])

# 4. Lookup the key associated with the value "New Jersey" and print it out.
# Hint 1: You will need to loop through the dictionary.
# Hint 2: remember you can use the .items() method to get the key and value.

for key, value in my_dict.items():
    if value == "New Jersey":
        print(key)

# 5. Add a new key value pair to the dictionary.
# Key: "country", Value: "USA"

my_dict["country"]= "USA"

# 6. Print out the dictionary.
print(my_dict)
# 7. Remove the key value pair with the key "city".
my_dict.pop("city")
# 8. Print out the dictionary.
<<<<<<< HEAD
print(my_dict)
# 9. Create a dictionary called cities with an key as the City name and values as a list that contains the state, population, and country.
=======

# 9. Create a dictionary called cities with an key as the City name and values as a dictionary that contains the state, population, and country.
>>>>>>> 65906ed8d0f28086dbc98c849d0d0b4918895f81
# use the following data:
# Trenton, New Jersey, 84,913, USA
# New York City, New York, 8,336,817, USA
# Los Angeles, California, 3,979,576, USA
# Chicago, Illinois, 2,693,976, USA
# Houston, Texas, 2,320,268, USA
# Phoenix, Arizona, 1,680,992, USA
# Philadelphia, Pennsylvania, 1,584,138, USA
# San Antonio, Texas, 1,547,253, USA
# San Diego, California, 1,423,851, USA
cities = {
    'Trenton': {'State': 'New Jersey', 'Population': 84913, 'Country': 'USA'},
    'New York City': {'State': 'New York', 'Population': 8336817, 'Country': 'USA'},
    'Los Angeles': {'State': 'California', 'Population': 3979576, 'Country': 'USA'},
    'Chicago': {'State': 'Illinois', 'Population': 2693976, 'Country': 'USA'},
    'Houston': {'State': 'Texas', 'Population': 2320268, 'Country': 'USA'},
    'Phoenix': {'State': 'Arizona', 'Population': 1680992, 'Country': 'USA'},
    'Philadelphia': {'State': 'Pennsylvania', 'Population': 1584138, 'Country': 'USA'},
    'San Antonio': {'State': 'Texas', 'Population': 1547253, 'Country': 'USA'},
    'San Diego': {'State': 'California', 'Population': 1423851, 'Country': 'USA'}
}



# 10. Print a table of the data using the pandas library.
# pip install pandas
import pandas as pd

cities_data = {
    'City': list(cities.keys()),
    'State': [info[0] for info in cities.values()],
    'Population': [info[1] for info in cities.values()],
    'Country': [info[2] for info in cities.values()]
}

df = pd.DataFrame(cities_data)
print(df)

# 11. Use the tabulate library to print out the table.
# pip install tabulate

from tabulate import tabulate

cities_data = [
    ['Trenton', 'New Jersey', 84913, 'USA'],
    ['New York City', 'New York', 8336817, 'USA'],
    ['Los Angeles', 'California', 3979576, 'USA'],
    ['Chicago', 'Illinois', 2693976, 'USA'],
    ['Houston', 'Texas', 2320268, 'USA'],
    ['Phoenix', 'Arizona', 1680992, 'USA'],
    ['Philadelphia', 'Pennsylvania', 1584138, 'USA'],
    ['San Antonio', 'Texas', 1547253, 'USA'],
    ['San Diego', 'California', 1423851, 'USA']
]

headers = ['City', 'State', 'Population', 'Country']

print(tabulate(cities, headers=headers, tablefmt='grid'))

# 12. Print out the population for the city of Chicago.

print(cities['Chicago']['Population'])

# 13. **Extra** An alternative to converting a dictionary into a pandas df then tabulate, you can use dictionary unpacking and tabulate.
# Dictionary unpacking is a new feature in Python 3.9 and allows you to unpack a dictionary into a list of dictionaries.
# You can then use tabulate to print out the table.

# In our case, {"City": city, **info} creates a new dictionary that includes a "City" key with the city name and all the key-value pairs from the info dictionary.

# For example, if city is "Chicago" and info is {"state": "Illinois", "Population": 2693976, "Country": "USA"}, the new dictionary will be {"City": "Chicago", "state": "Illinois", "Population": 2693976, "Country": "USA"}. This is the same as {"City": city, **info}.
# The ** operator unpacks the info dictionary into the new dictionary

# Transform the data

# Print the table using tabulate


# 12. How many cities have a population greater than 1 million? Use a for loop to iterate through the dictionary.
count_cities_greater_than_1m = 0

for city_info in cities.values():
    population = city_info['Population']
    if population > 1000000:
        count_cities_greater_than_1m += 1

print(f"The number of cities with a population greater than 1 million is: {count_cities_greater_than_1m}")
# 13.  How many cities are in the USA? Use .items() to get a list of tuples. Use a for loop to iterate through the list of tuples.
# Hint 1: You will need to use the second item in the tuple. The second item is a dictionary. IE. for city, info in cities.items():
count_cities_in_usa = 0

for city, info in cities.items():
    country = info['Country']
    if country == 'USA':
        count_cities_in_usa += 1

print(f"The number of cities in the USA is: {count_cities_in_usa}")
#Finished