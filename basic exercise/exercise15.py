"""Exercise 15: Write a function called 
exponent(base, exp) that returns an int value
 of base raises to the power of exp.ote
   here exp is a non-negative integer,
   and the base is an integer."""

def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result*base
        num-=1
    print(result)

#test
exponent(5,4)
exponent(2,5)