#This is A simple python program that converts days into hours minutes and seconds using variables.

#Let the user know what the program does.
print("This program uses the number of days that you enter and turns it into hours, minutes, and seconds.")

#Ask the user to input the number of days.
days =int(input("Please enter the total number of days: "))

#Establish the amount of hours in a day, minutes in an hour, and seconds in a minute.
hours = days * 24
minutes = hours * 60
sec = minutes * 60

#Display the users input converted into hours minutes and seconds.
print("All days:", days)
print("All Hours:", hours)
print("All Minutes:", minutes)
print("All Second:", sec)