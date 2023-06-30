"""Display numbers from a list using loop
Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop"""

# Approach:
"""Use for loop to iterate each item of a list
Use break statement to break the loop if the current number is greater than 500
use continue statement move to next number if the current number is greater than 150
Use number % 5 == 0 condition to check if number is divisible by 5
"""
numbers = [12, 75, 150, 180, 145, 525, 50]
#iterate each item of a list
for item in numbers:
    if item>500:
        break
    elif item>150:
        continue
    # check if number is divisible by 5
    elif item%5==0:
        print(item)