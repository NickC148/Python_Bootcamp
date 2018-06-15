### 2-8-1 Operating System Interface ###
# The os module provides dozens of functions for interacting with the operating system.
# These may differ from Windows to Linux or Mac. It is preferable to use import os and avoid
# from os import *.

import os

# There is also a shutil module with a higher level interface simialr to the os module which
# may be easier to use at times.

import shutil


### 2-8-2 File Wildcards ###
# The glob module provides a function for making file lists from directory wildcard searches.
# This is very useful for writing utility scripts.

import glob
glob.glob('*.py')


### 2-8-3 Command Line Arguments ###
# Common utility scripts often need to process command line arguments. These arguments are stored
# in the sys module’s argv attribute as a list. Starting python with extra arguments,
# say python - this is more than one. There are many treasures im module sys, for example stdout
# or stderr could be used for writing info or errors. You could even use the dread exit to terminate
# the session. In programs running using exception handling, exit is generally to be avoided.

import sys
print sys.argv
sys.stdout.write('info\n')
sys.stderr.write('error\n')
sys.exit(1)


### 2-8-4 String Pattern Matching ###
# The re module provides regular expression tools for advanced string processing. For complex matching
# and manipulation, regular expressions offer succinct, optimized solutions. Unfortunately they are
# quite often about as readable as an APL program.

import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

# When only simple capabilities are needed, string methods are preferred because they are easier to
# read and debug.

'cat in the the hat'.replace('the the', 'the')


### 2-8-5 Mathematics ###
# The math module gives access to the underlying C library functions for floating point math.

import math
math.cos(math.pi / 4.0)
# 0.7071067811865476
math.log(1024, 2)
# 10

# The random module provides tools for making random selections.

import random
alist = ['banana', 'apple', 'blackberry']
random.choice(alist)
random.random()
random.randrange(6)


### 2-8-6 Internet Access ###
# There are a number of modules for accessing the internet and processing internet protocols.
# Two of the simplest are urllib2 for retrieving data from URLs and smtplib for sending mail.

import urllib2
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'EST' in line or 'EDT' in line:
        print line
# <BR>May. 14, 04:41:01 AM EDT            Eastern Time

# - (Note that this second example needs a mailserver running on localhost.)
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
                """To: jcaesar@example.org
From: soothsayer@example.org
Beware the Ides of March.
""")
server.quit()


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


### 2-8-8 Data Compression ###
# Common data archiving and compression formats are directly supported by modules including: zlib,
# gzip, bz2, zipfile and tarfile.

import zlib
s = 'witch which has which witches wrist watch'
print len(s)
t = zlib.compress(s)
print len(t)
print zlib.decompress(t)
# 226805979


### 2-8-9 Performance Measurement ###
# Some Python users develop a deep interest in knowing the relative performance of different approaches
# to the same problem. Python provides a measurement tool that answers those questions immediately.

# For example, it may be tempting to use the tuple packing and unpacking feature instead of the
# traditional approach to swapping arguments. The timeit module quickly demonstrates a modest
# performance advantage.

from timeit import Timer
print Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# 0.0320846332396
print Timer('a,b = b,a', 'a=1; b=2').timeit()
# 0.026504411628

# In contrast to timeit‘s fine level of granularity, the profile and pstats modules provide tools for
# identifying time critical sections in larger blocks of code.


### 2-8-10 Quality Control ###
# One approach for developing high quality software is to write tests for each function as it is
# developed and to run those tests frequently during the development process.

# The doctest module provides a tool for scanning a module and validating tests embedded in a
# program’s docstrings. Test construction is as simple as cutting-and-pasting a typical call along
# with its results into the docstring. This improves the documentation by providing the user with an
# example and it allows the doctest module to make sure the code remains true to the documentation.


def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print average([20, 30, 70])
    40.0
    """
    return sum(values, 0.0) / len(values)


import doctest
doctest.testmod()   # automatically validate the embedded tests

# The unittest module is not as effortless as the doctest module, but it allows a more comprehensive
# set of tests to be maintained in a separate file.

import unittest


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)


unittest.main()  # Calling from the command line invokes all tests


### 2-8-11 Batteries Included ###
# Python has a “batteries included” philosophy. This is best seen through the sophisticated and robust
# capabilities of its larger packages. For example:

# The xmlrpclib and SimpleXMLRPCServer modules make implementing remote procedure calls into an almost
# trivial task. Despite the modules names, no direct knowledge or handling of XML is needed.

# The email package is a library for managing email messages, including MIME and other RFC 2822-based
# message documents. Unlike smtplib and poplib which actually send and receive messages, the email
# package has a complete toolset for building or decoding complex message structures (including
# attachments) and for implementing internet encoding and header protocols.

# The xml.dom and xml.sax packages provide robust support for parsing this popular data interchange
# format. Likewise, the csv module supports direct reads and writes in a common database format.
# Together, these modules and packages greatly simplify data interchange between Python applications
# and other tools.

# Internationalization is supported by a number of modules including gettext, locale, and the codecs
# package.
