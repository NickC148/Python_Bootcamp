import math

name = raw_input("What's your name? ")
print ("Hello, " + name + "!")
age = raw_input("How old are you today? ")
print ("Ah, so you're at least " + str(int(age) *
                                       365.25 * 24 * 60 * 60) + ' seconds old...')
