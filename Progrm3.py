'''
Program 3
https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

Program Description:
Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

xtras:

Instead of printing the elements one by one, make a new list that has all the
elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from
the original list a that are smaller than that number given by the user.
'''
####### Python COde Starts from Here #############

#create a Empty List

x = list()

#Ask the user how many numbers he needs to store in list.

number =int( input("Enter the total count present in the list"))

for i in range(number):
	x.append(int(input("Enter Number:" )))

#List created.

#Ask the user the maximum number and print the numbers less than that 
max_number = int(input("Max. Number"))

 #Create an empty second list
y= list()

for i in x:
    if i < max_number:
	    y.append(i)
#

print ("\nOriginal List ",x)
print("Maximum Number",max_number)
print("Modified List",y)

