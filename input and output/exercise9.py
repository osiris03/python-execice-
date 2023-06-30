import os
"""Write a program to check if the given file is empty or not"""


# first solution
# with open('file_dict/text.txt','r') as f:
#     lines = f.read()
#     for line in lines:
#         if line == " ":
#             print('file is empty')
#         else:
#             print('file is not empty')

# second solution

size = os.stat("text.txt").st_size
if size == 0:
    print('file is emp')