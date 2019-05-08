```
Sample Input #1:
meals = [
  Meal("American", ["lettuce", "cheese", "olives", "tomato"] ),
  Meal("Mexican", ["lettuce", "cheese", "pepper", "tomato"] ),
  Meal("French", ["lettuce", "cheese", "pepper", "tomato"] ),
  Meal("Continental", ["lettuce", "cheese", "olives", "tomato"] )
]


Sample Output #1:
2


Problem Statement :

make a program that list unique dishes. Dishes with same ingredients irirespective of order given will be considered as single dish

```
from collections import defaultdict
dice = defaultdict(list)
for key in mydict.keys():
    for values in mydict.values():
        #print(values,key)
        dice[key].append(values)
        
totalfoods = list(dice.values())
print(len(totalfoods))
