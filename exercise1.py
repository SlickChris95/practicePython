'''
Create a program that asks the user to enter
their name and their age. Print out a message
addressed to them that tells them the year that
they will turn 100 years old.
'''

import datetime

now = datetime.datetime.now()
print('Enter your name')
name = input()
print('Enter your age')
age = input()
print(name + ', In ' + str((100 - int(age)) + now.year) + ' you will be 100!')
print(now.year)
