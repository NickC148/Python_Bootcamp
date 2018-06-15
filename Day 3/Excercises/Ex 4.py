# Using the table below:

#   ItemNo  Description       No  Cost Each
#   IT445   Snark bits        12       2.79
#   IT123   Pistle dibs        5      11.13
#   BK001   Yannie not Laurel  1     123.15

# a. Use a tuple assignment create the variables item_no, desc, no, cost_each using a range.
# b. Create an item_list of tuples each containing the values for each line.
# c. Looping through the list, for each tuple use the variables above as indices, calculating the
# amount and print a line. Using a pre initialised total sum the amounts.
# d. Print the total.

# A
items = []
for x in range(3):
    items.append({'ItemNo': None, 'Description': None,
                  'No': None, 'Cost Each': None})

# B
items[0]['ItemNo'] = 'IT445'
items[0]['Description'] = 'Snark bits'
items[0]['No'] = 12
items[0]['Cost Each'] = 2.79

items[1]['ItemNo'] = 'IT123'
items[1]['Description'] = 'Pistle dibs'
items[1]['No'] = 5
items[1]['Cost Each'] = 11.13

items[2]['ItemNo'] = 'BK001'
items[2]['Description'] = 'Yannie not Laurel'
items[2]['No'] = 1
items[2]['Cost Each'] = 123.15

item_list = []

for x in range(3):
    item_list.append(items[x])

# C
total = 0
for y in item_list:
    sumT = y['No'] * y['Cost Each']
    total = total + sumT
    print 'The sum for {0} is {1}'.format(y['Description'], sumT)

# D
print 'The total for everything is {0}'.format(total)
