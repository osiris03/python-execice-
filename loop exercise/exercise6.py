"""Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop."""


"""
Set counter = 0
Run while loop till number != 0
In each iteration of loop
Reduce the last digit from the number using floor division ( number = number // 10)
Increment counter by 1
print counter
"""

number = int(input("Enter a number\n"))
num=0
counter =0
while number !=0:
    # floor division
    # to reduce the last digit from number
    number//=10

    # increment counter by 1
    counter+=1
print(counter)