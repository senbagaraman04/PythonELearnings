'''
 
 https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

 Ask the user for a string and print out whether this string is a palindrome or not. 
 (A palindrome is a string that reads the same forwards and backwards.)



'''

_author_="Senbagaraman"
_date_="12/10/2018"

def palin(string):
	if(string==string[::-1]):
      print("The string is a palindrome")
	else:
      print("The string isn't a palindrome")



print("Enter a String:")
string = input()
palin(string)

