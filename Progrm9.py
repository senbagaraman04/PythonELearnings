'''
 https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
 Guessing Game One   
Exercise 9 (and Solution)
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.



'''

_author_="Senbagaraman"
_date_="1/18/2019"
_email_"senbagaraman04(at)gmail(dot)com"

#Code Starts Here 
#Guessing game
import random
print("Guessing Game")

print ("** Guess a number(from 0 t0 100) : and compare the same with the computer")

def Random_GuessCalculate(user,bot):
	if user == bot:
		print ("Draw!!")
	elif user > bot:
		print ("To far")
	elif print ("To low")


inpA = int(input("Guess a number"))

inpB = random.randint(0,100)

Random_GuessCalculate(inpA,inpB)

