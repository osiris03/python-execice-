"""Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers"""

n = int(input("give a number"))



def palindrome(n):
    print("original number",n)
    original_num = n

    reverse_num = 0
    while n > 0:
        reminder = n%10
        reverse_num=(reverse_num*10)+reminder
        n=n//10
    
    if original_num == reverse_num:
        print("given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(n)