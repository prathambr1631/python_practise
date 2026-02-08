#Dictionary
#list of 5 cities in Karnataka and their famous dishes.
karnataka_cities = {
    "Bangalore": "Bisi Bele Bath",
    "Mysore": "Mysore Pak",
    "Mangalore": "Kori",
    "Hubli": "Dosa",
    "Belgaum": "Papdi"
}

#Adding new city 
print("Adding.....")
karnataka_cities["Bidadi"] = "Thathe Idly" 
print(karnataka_cities)

#Updating
print("Updating.....")
karnataka_cities['Bidadi'] = "Thatte Idli"
print(karnataka_cities)

#Removing one city
print("Removing.....")
karnataka_cities.pop("Belgaum")
print(karnataka_cities)

#Accessing only Keys
print("Accessing only Keys.....")
print(karnataka_cities.keys())

#Accessing only Values
print("Accessing only Values.....")
print(karnataka_cities.values())


#2ND Dictionary 
#LIst of 2 friends 
friend1 = {
    "Name": "Chimay",
    "fav_sub" : "Maths",
    "fav_food" : "Chapathi"
}

friend2 = {
    "Name": "Adarsh",
    "fav_sub" : "Science",
    "fav_food" : "Palav"
}

#Printing the favourite food of friend1
print("Favourite food of friend1: ", friend1["fav_food"])