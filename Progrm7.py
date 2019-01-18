'''
 
https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes 
this list a and makes a new list that has only the even elements of this list in it.

Discussion
Concepts for this week:

List comprehensions
List comprehensions
The idea of a list comprehension is to make code more compact to accomplish tasks involving lists. Take for example this code:

  years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
  ages = []
  for year in years_of_birth: 
    ages.append(2014 - year)
And at the end, the variable ages has the list [24, 23, 24, 24, 22, 23]. What this code did was translate the years of birth into ages, and it took us a for loop and an append statement to a new list to do that.

Compare to this piece of code:

  years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
  ages = [2014 - year for year in years_of_birth]
The second line here - the line with ages is a list comprehension.

It accomplishes the same thing as the first code sample - at the end, the ages variable has a list containing [24, 23, 24, 24, 22, 23], the ages corresponding to all the birthdates.

The idea of the list comprehension is to condense the for loop and the list appending into one simple line. Notice that the for loop just shifted to the end of the list comprehension, and the part before the for keyword is the thing to append to the end of the new list.



'''

_author_="Senbagaraman"
_date_="12/26/2018"

'''
 
https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes 
this list a and makes a new list that has only the even elements of this list in it.

Discussion
Concepts for this week:

List comprehensions
List comprehensions
The idea of a list comprehension is to make code more compact to accomplish tasks involving lists. Take for example this code:

  years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
  ages = []
  for year in years_of_birth: 
    ages.append(2014 - year)
And at the end, the variable ages has the list [24, 23, 24, 24, 22, 23]. What this code did was translate the years of birth into ages, and it took us a for loop and an append statement to a new list to do that.

Compare to this piece of code:

  years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
  ages = [2014 - year for year in years_of_birth]
The second line here - the line with ages is a list comprehension.

It accomplishes the same thing as the first code sample - at the end, the ages variable has a list containing [24, 23, 24, 24, 22, 23], the ages corresponding to all the birthdates.

The idea of the list comprehension is to condense the for loop and the list appending into one simple line. Notice that the for loop just shifted to the end of the list comprehension, and the part before the for keyword is the thing to append to the end of the new list.



'''

_author_="Senbagaraman"
_date_="12/26/2018"


_author_="Senbagaraman"
_date_="1/17/2019"

inp = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

oup = list()
print(inp)

for i in inp:
    if i%2 == 0:
        oup.append(i)
        
print(oup)





