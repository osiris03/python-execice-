"""Exercise 5: Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. If numbers are different then return False."""

def lastegaltofirst(t):
    for i in range(0,len(t)):
        if t[0] == t[len(t)-1]:
            return True
        else:
            return False

number_x = [10,20,30,40,10]
number_y = [75,64,34,74,32]

print("Given list",number_x,"\n result is \t",lastegaltofirst(number_x))
print("Given list",number_y,"\n result is \t",lastegaltofirst(number_y))