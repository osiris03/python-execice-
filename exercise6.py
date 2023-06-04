"""Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5"""


def number_divisible_five(t):
    for i in range(0,len(t)):
        if t[i]%5==0:
            print(t[i])

n= [10,20,33,46,55]

print("Given list is  ",n ,"\ndivisible by 5\n")
number_divisible_five(n)
