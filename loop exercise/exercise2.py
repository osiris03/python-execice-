"""Print the following pattern
Write a program to print the following number pattern using a loop."""


"""
Approach:

Decide the row count, i.e., 5, because the pattern contains five rows
Run outer for loop 5 times using for loop and range() function
Run inner for loop i+1 times using for loop and range() function
In the first iteration of the outer loop, the inner loop will execute 1 time
In the second iteration of the outer loop, the inner loop will execute 2 time
In the third iteration of the outer loop, the inner loop will execute 3 times, and so on till row 5
print the value of j in each iteration of inner loop (j is the the inner loop iterator variable)
Display an empty line at the end of each iteration of the outer loop (empty line after each row)
"""

# Decide the row count. (above pattern contain row)

row = int(input("Enter Pattern"))
# start:1
# stop: row+1(range never include stop number in result)
#step:1
#run loop row times

for i in range(1,row+1,1):
    for j in range(1,i+1):
        print(j, end=" ")
    print("")
