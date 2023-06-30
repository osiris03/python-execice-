# For example, If the given int is 7536, the output shall be “6 3 5 7“,
# with a space separating the digits.



n = int(input("give an integer number "))

print(" Given number",n)
def reverse_digit(n):
    while n >0:
        """get the last digit"""
        digit = n%10
        # remove the last digit and repeat the loop
        n = n//10
        print(digit,end='')

"""test"""
n =78939
 
reverse_digit(n)
