"""Exercise 4: Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
Note: n must be less than the length of the string."""

def remove_chars(n,b):
    print(n[b:])


# n=(input("give a string\n"))
# b = int(input("give a number of char your want to remove starting from zero\n"))
remove_chars("pynative",2)
