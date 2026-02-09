#Conditional Statements
#Write a program to check if someone is eligible for a bus pass. If they are below 5 years, the bus pass is free. If they are 60 years or older, they get a senior citizen discount. Otherwise, they pay the full price.
age = int(input("Enter your age: "))
if age <= 5:
    print("You are eligible for a free bus pass.")
elif age >= 60:
    print("You are eligible for a senior citizen discount on your bus pass.")
else:
    print("You need to pay the full price for your bus pass.")  


#Alaram for Breakfast, Lunch and Dinner
time = int(input("Enter the time: "))
if time == 8:
    print("It's time for breakfast!")
elif time == 13:
    print("It's time for lunch!")
elif time == 20:
    print("It's time for dinner!")
else:
    print("It's not time for any meal yet.")


 #Write a program that checks whether a person is eligible for a library membership. If they are under 18, they get a student membership. If they are 60 or older, they get a senior citizen membership. Otherwise, they get a regular membership.
age = int(input("Enter your age: "))
if age < 18:
    print("You are eligible for a student library membership.")
elif age >= 60:
    print("You are eligible for a senior citizen library membership.")
else:
    print("You are eligible for a regular library membership.")
