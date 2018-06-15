### 2-8-7 Date and Times ###
# The datetime module supplies classes for manipulating dates and times in both simple and complex ways.
# While date and time arithmetic is supported, the focus of the implementation is on efficient member
# extraction for output formatting and manipulation. The module also supports objects that are timezone
# aware. Here we will do a from datetime import date.

from datetime import date
now = date.today()
print now
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
#'05-14-18. 14 May 2018 is a Monday on the 14 day of May.'
birthday = date(1964, 7, 31)
age = now - birthday
print age.days
