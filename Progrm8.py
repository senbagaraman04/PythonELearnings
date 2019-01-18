'''
 https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
 
 Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
 print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
Discussion
Concepts for this week:

While loops
Infinite loops
Break statements




'''

_author_="Senbagaraman"
_date_="1/18/2019"
_email_ = "senbagaraman04(at)gmail(dot)com"

import random

#R-1,P-2,S-3

def call_playGameFunc(user,bot):    
	if user == bot:
		print ("Draw")
	elif (user==1 and bot!=2) or (user==2 and bot!=3) or (user==3 and bot!=1):
	    print ("you won")
	else:
	    print("You Lose")

#print "Rock Paper and Scissor game"

#print "Enter the your choice:"

#print "1 if Rock"

#print "2 if Paper"

#print "3 if Scissor"

while(True):
    UserA = int(input(""))

#Comment the following two line if the userB is from computer
#print "Enter User B value"
    UserB = int(input(""))

#Uncomment the below line if UserB is computer
#UserB = random.randint(1,4)

    call_playGameFunc(UserA,UserB)
    next_turn = input("Do you need to play again? y/n")
    if next_turn != "y":
        break;

