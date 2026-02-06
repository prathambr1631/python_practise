#Sets
my_fav = {"Avacado","Apple","Banana"}
friend_fav = {"Watermelon","Mango","Banana","Apple"}

#Set operations
union = my_fav | friend_fav
print("Union: ", union)
intersection = my_fav & friend_fav
print("Intersection: ", intersection)
difference = my_fav - friend_fav
print("Difference: ", difference)
sys_difference = my_fav^friend_fav
print("Symmetric Difference: ",sys_difference)

#Set Methods
print("Discarding a element: ",my_fav.discard("Apple"))
print("clearing set: ", my_fav.clear())