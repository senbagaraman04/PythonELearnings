 '''
 
 
 #https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
 Create a program that asks the user for a number and then prints out a list
 of all the divisors of that number. (If you don’t know what a divisor is,
 it is a number that divides evenly into another number. 
 For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

 '''

 _author_="Senbagaraman"
 _date_="12/9/2018"

 dictlist = list()

 num = int(input('Enter a number'))

 for i in range(num):
	if num % i == 0:
		dictlist.append(i)
#

print (dictlist)