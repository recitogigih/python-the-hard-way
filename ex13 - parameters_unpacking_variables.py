from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

""" 
Run the program like this (and you must pass three command line arguments):
   
Exercise 13 Session
$ python3.6 ex13.py first 2nd 3rd
"""