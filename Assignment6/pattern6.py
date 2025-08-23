# WAP to print the following pattern
#        1
#      1 2 3
#    1 2 3 4 5
#  1 2 3 4 5 6 7
#1 2 3 4 5 6 7 8 9
k=2
for i in range (1,5+1):
    for j in range (1,6-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(1,i):
        if(i>3 and j==1):
            print(k,end=" ")
        else:
            k+=1
            print(k,end=" ")
    print()
    
    