# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

a = int(input("give the first number\n"))
b = int(input("give the second number\n"))

def product(a,b):
    print("the product is", a*b) if a*b <= 1000 else print("the sum is ,", a+b)

print(a,b)
product(a,b)
