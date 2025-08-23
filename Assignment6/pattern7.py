# WAP to print the following pattern
#            A
#          A B C
#        A B C D E 
#      A B C D E F G
#    A B C D E F G H I
s=66
for i in range (1,6):
    for j in range(1,6-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    for j in range(1,i):
        if(i>3 and j==1):
            print(chr(s),end=" ")
        else:
            s+=1
            print(chr(s),end=" ")
        
    print()