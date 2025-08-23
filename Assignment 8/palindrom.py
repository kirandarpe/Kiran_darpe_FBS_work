# write a program to check number is palindrome or not
def pal(num):
    rev=0
    temp=num
    while(num>0):
        d=num%10
        num//=10
        rev=rev*10+d
    if(temp==rev):
        print(f"{rev}: is palindrome")
    else:
        print("number is not palindrom")
num=int(input("enter the number:"))
pal(num)
