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

# Create a list for the names of the months.

Months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

# Given the dates '20180304', '20171031', '20160602', '19951223'
# (dates in the format 'YYYYMMDD'), write a function to be able to
# convert these dates to the form 1st January, 1901. The (st nd rd th)
# is called the ordinal suffix, we want the day without leading zero
# ending in its ordinal suffix, the written month with a comma and the
# full year.

dates = ['20180304', '20171031', '20160602', '19951223']


def convert_date():
    formatted_dates = []
    for date in dates:
        year = date[0:4]
        numeric_month = date[4:6]
        numeric_day = date[6:8]

        day = format_Day(numeric_day)

        month = format_month(numeric_month)

        newDateString = day + ' ' + month + ', ' + year
        formatted_dates.append(newDateString)
    return formatted_dates


def format_Day(day):
    day = get_ordinal_suffix(day)
    if day[0] == '0':
        day = day.replace('0', '')

    return day


def get_ordinal_suffix(day):
    if day[1] == '1':
        return day + 'st'
    elif day[1] == '2':
        return day + 'nd'
    elif day[1] == '3':
        return day + 'rd'
    else:
        return day + 'th'


def format_month(month):
    # Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return Months[int(month) - 1]


newDates = convert_date()
print newDates

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
