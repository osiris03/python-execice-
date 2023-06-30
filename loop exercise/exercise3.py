"""Calculate the sum of all numbers from 1 to a given number
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)"""

#first solution look k as  finte sum of n number
n=int(input("Enter number \n"))
k=(n*(n+1))/2
print("the sum of 1 to ",n,"is: ",k)

# second solution

"""Approach 1: Use for loop and range() function

Create variable s = 0 to store the sum of all numbers
Use Python 3’s built-in function input() to take input from a user
Convert user input to the integer type using the int() constructor and save it to variable n
Run loop n times using for loop and range() function
In each iteration of a loop, add current number (i) to variable s
Use the print() function to display the variable s on screen"""
s=0
for i in range(1,n+1):
    s+=i
print("the sum of 1 to",n,"is: ",s)


