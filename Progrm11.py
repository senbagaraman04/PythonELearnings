'''
 https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

 Ask the user for a number and determine whether the number is
 prime or not. (For those who have forgotten, a prime number is
 a number that has no divisors.). You can (and should!) use your
 answer to Exercise 4 to help you. Take this opportunity to practice
 using functions, described below.




'''

_author_="Senbagaraman"

def findPrime(number):
	#print ("The number you have entered is",number)
	divCount = 0
	for x in range(1,number+1):
		#print("Number = ",number,"& x = ",x)
		if number % x == 0:
			#print (The Values are )
			divCount = divCount+1
		#else:
			#Donothing
	#print ("The Divison Count",divCount)

	if divCount == 2:
		print ("Landed on Moon")
	else:
		print ("Nope, just a miss, but landed on stars")



inp = int(input("Enter a number"))

ans = findPrime(inp)


