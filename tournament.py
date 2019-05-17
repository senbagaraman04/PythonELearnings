'''
Tournament
There is a tournament between two teams. The tournament consists of N rounds. Each team has N competitors. Each competitor has a power between a-z and if the power of two competitors matches in a round then that round will going to be drawn. You have to find the maximum number of draw rounds possible.

Input Format:

The first line of input contains T, denotes the total number of test cases.

Each test case contains an Integer N denotes the number of rounds.

Next two lines will contain a string of lowercase letters of length N denoting the power of N competitors of both teams.

Output Format:

Output the answer in a new line.

Constraints:

1 <= T <= 10
1 <= N <= 105 
String will contain only lowercase alphabet

Sample Input
2
4
aabc
zcaa
5
pqrrs
rsptr

Sample Output
3
4


Explanation
Testcase 1 - 

    Possible draw matches are possible between a, a, c.

Testcase 2 -

    Possible draw matches are possible between r, s, p, r.
'''




'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
test = int(input())
for i in range(test):
    count1=0
    count = int(input())
    teamA = input()
    teamB = input()
    for i in teamA:
        if i in teamB:
            #print (i,end='')
            count1 = count1+1
    print(count1)
