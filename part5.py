'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month
'''

#start writing your code below

month = input("Enter a month: ")

if month == ("January"):
 print("This month has 31 days.")
elif month == ("january"):
  print("This month has 31 days.")
elif month == ("March"):
  print("This month has 31 days.")
elif month == ("march"):
  print("This month has 31 days.")
elif month == ("May"):
  print("This month has 31 days.")
elif month == ("may"):
  print("This month has 31 days.")
elif month == ("july"):
  print("This month has 31 days.")
elif month == ("July"):
  print("This month has 31 days.")
elif month == ("August"):
  print("This month has 31 days.")
elif month == ("august"):
  print("This month has 31 days.")
elif month == ("october"):
  print("This month has 31 days.")
elif month == ("October"):
  print("This month has 31 days.")
elif month == ("December"):
  print("This month has 31 days.")
elif month == ("december"):
  print("This month has 31 days.")
elif month == ("april"):
  print("This month has 30 days.")
elif month == ("April"):
  print("This month has 30 days.")
elif month == ("June"):
  print("This month has 30 days.")
elif month == ("june"):
  print("This month has 30 days.")
elif month == ("Spetember"):
  print("This month has 30 days.")
elif month == ("september"):
  print("This month has 30 days.")
elif month == ("November"):
  print("This month has 30 days.")
elif month == ("november"):
  print("This month has 30 days.")
elif month == ("February"):
  print("This month has either 28 or 29 days.")
elif month == ("february"):
  print("This month has either 28 or 29 days.")
else:
  print("This is not a month.")