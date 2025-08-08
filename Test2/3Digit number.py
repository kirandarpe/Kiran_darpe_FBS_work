number=int(input("enter the number:"))
temp=number
a=temp//100
temp=temp%100
b=temp//10
c=temp%10
if(a is b*2):
    if( a//c==c):
       print("Yes,you have done it")
    else:
        print("please try again")
else:
    print("pelead try again")