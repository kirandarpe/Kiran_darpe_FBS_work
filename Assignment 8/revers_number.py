# write a program to find revers number
def rev(num):
    rev=0
    temp=num
    while(num>0):
        d=num%10
        rev=rev*10+d
        num//=10
    if(temp==rev):
        print(f"{rev}: is revers")
num=int(input("enter the number:"))
rev(num)