"""Print list in reverse order using a loop"""


"""Approach 1: Use the built-in function reversed() to reverse the list

Approach 2: Use for loop and the len() function
"""

list = [10, 20, 30, 40, 50]

list2=reversed(list)
for item in list2:
    print(item)
