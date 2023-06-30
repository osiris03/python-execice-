"""Exercise 10: Create a new list from a two list using the following condition
Create a new list from a two list using the following condition

Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list."""


def merge_list(list1, list2):
    list_result = [ ]
    for j in list2:
        if j%2 != 0:
            list_result.append(j)
    for j in list1:
        if j%2 == 0:
            list_result.append(j)
    
    return list_result

lista = [10, 20, 25, 30, 35]
listo = [40, 45, 60, 75, 90]
print("the merging list is :",merge_list(lista, listo))

