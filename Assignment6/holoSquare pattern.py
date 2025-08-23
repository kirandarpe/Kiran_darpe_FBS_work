# Wap to print holo square
#   * * * * *
#   *       *
#   *       *
#   *       *
#   *       *
#   * * * * *
for i in range(1,6+1):
    for j in range(1,6):
        if(j==1 or j==5 or i==1 or i==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()