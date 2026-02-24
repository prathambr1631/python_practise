# This program will print the numbers from 1 to 10 using a for loop.
for i in range (1, 11):
    print(i,end=" ")

#Write a for loop that prints all multiples of 3 between 1 and 30.
for j in range (1, 31):
        print(f"3x{j}={3*j}")

#Write a program using a for loop that calculates the sum of numbers from 1 to 10.
total = 0
for k in range (1, 11): 
    total += k
print(f"The sum of numbers from 1 to 10 is: {total}")

#Write a program that takes your name as input and prints each letter of your name using a for loop.
name = "Pratham"
for letter in name:
    print(letter, end="")