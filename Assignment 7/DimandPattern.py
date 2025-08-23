#Wap a program to print holo dimand pattern
for i in range (1,6):
    for j in range (1,6-i+1):
        print("",end=" ")
    for j in range (1,i+1):
        if(j==1 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(1,6):
    for i in range(1,i+1):
        print("",end=" ")
    for j in range(1,6):
        if(j==1 or i+j==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()