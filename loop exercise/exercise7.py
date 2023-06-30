"""Print the following pattern
Write a program to use for loop to print the following reverse number pattern"""


"""
Approach:
Set row = 5 because the above pattern contains five rows
create an outer loop to iterate numbers from 1 to 5 using for loop and range() function
Create an inner loop inside the outer loop in such a way that in each iteration of the outer loop, the inner loop iteration will be reduced by i. i is the current number of an outer loop
In each iteration of the inner loop, print the iterator variable of the inner loop (j)
Note:

In the first iteration of the outer loop inner loop execute five times.
In the second iteration of the outer loop inner loop execute four times.
In the last iteration of the outer loop, the inner loop will execute only once
"""
row = int(input("Enter Pattern "))
# start:0
# stop: row+1(range never include stop number in result)
#step:0
#run loop row times

for i in range(0,row+1):
    for j in range(row-i,0,-1):
        print(j, end=" ")
    print("")