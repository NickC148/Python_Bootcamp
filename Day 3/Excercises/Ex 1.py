# Take this list a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and print out all
# the elements of the list that are less than 5. Instead of printing the elements
# one by one, make a new list that has all the elements less than 5 from this list
# in it and print out this new list.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = []

for num in a:
    if num < 5:
        b.append(num)

print b
