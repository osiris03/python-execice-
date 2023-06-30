"""Print the following pattern:
 1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 """

row =5
for i in range(row+1):
    for j in range(i):
        print(i,end="")
    print("")
