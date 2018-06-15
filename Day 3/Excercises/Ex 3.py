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
    Months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    return Months[int(month) - 1]


newDates = convert_date()
print newDates
