# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

n = str(input("write a word\n"))

for i in range(0, len(n)):
    if i%2==0:
        print(n[i])

 


    
