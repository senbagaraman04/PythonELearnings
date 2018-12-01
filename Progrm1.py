#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

#Exercise 1 (and Solution)
#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Date: 12/1/2018


print("Enter your Name")
name = input('')
print("Enter your age")
age = input('')
age = int(age) #converting string(age) into integer 

#Calculates the year when he/she will turn into 100

#Assumes the current year as 2018 :
curr_year = 2018
rem_age = 100 - age  #calculates the difference of age from 100
year_hundred = curr_year + rem_age
#Prints the year where the user will attain 100

print("By,",year_hundred,"you will attain 100 years")

###########################