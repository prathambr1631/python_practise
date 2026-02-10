# While Loops
# Write a program that counts from 1 to 10 using a while loop.
i = 1
while i <= 10:
    print(i)
    i += 1

# Write a program that prints the first 20 odd numbers using a while loop.
j = 1
while j <= 20:
    if j % 2 != 0:
        print(j)
    j += 1

#Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" after the countdown is over.
k = 10
while k >= 1:
    print(k)
    k -= 1
print("Happy New Year!")

#Write a program that simulates a bus ticket booking system. The bus has 8 seats. Each time a seat is booked, the available seats decrease. When there are no seats left, the loop stops and displays a message saying "All seats are booked."
l = 8
while l >= 0:
  print(f"Number of seats available: {l}")
  l -= 1
  if l < 0:
    break
print("No more seats available!")