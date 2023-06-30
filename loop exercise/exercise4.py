"""Write a program to print multiplication table  of a given number """



"""
approach:
Set n =2
Use for loop to iterate the first 10 numbers
In each iteration, multiply 2 by the current number.( p = n*i)
Print p
"""
n = int(input("Enter a number"))

for i in range(1,10+1):
    print(i*n)
