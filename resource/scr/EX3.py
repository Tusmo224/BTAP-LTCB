"""3. Write a Python program to get a string made of the first 2 and last 2 characters of a given
string. If the string length is less than 2, return the empty string instead."""

your_string = input('Enter your string: ')
if len(your_string) < 2:
    print(' ')
if len(your_string) > 2:
    print(your_string[0:2]+your_string[-2:])
if len(your_string) == 2:
    print(your_string*2)
