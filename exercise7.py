"""Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string."""


# def substring_occurency(s,w):
#     k=0
#     for i in range(0,len(s)):
#         if s[i] == w:
#             k = i+1
#     return k

str_x = "Emma is good developer. Emma is a writer"
d= "Emma"
# z= substring_occurency(str_x,d)
# print(d," appeared ",z,"times")


print("Emma appeared",str_x.count("Emma"))