"""4. Write a Python program to get a string from a given string where all occurrences of its first
char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'"""

string4 = input('Enter a bt4 string: ')
first_char = string4[0]
rest_char = string4[1:]
modifiedstring = string4.replace(first_char,"$")
final_string = first_char + modifiedstring[1:]
print(final_string)
