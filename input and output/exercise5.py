"""Accept a list of 5 float numbers as an input from the user"""
i=1
list =[]
while i<=5:
    print('give the number ',i)
    num=float(input())
    list.append(num)
    i+=1
print('User List',list)
