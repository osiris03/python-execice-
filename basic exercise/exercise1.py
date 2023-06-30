# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
previous_num = 0
for i in range(10):
    print("current number:",i ,"previous number:",i-1 , "sum:", 2*i-1)