# write a program to check given number is armstrong or not use multiple function
def arm(num):
    temp=num
    count=0
    while(temp>0):
        temp//=10
        count+=1
    return count
def ar(num):
    temp=num
    s=0
    while(temp>0):
        d=temp%10
        temp//=10
        s+=d**arm(num)
    return s
def con(num):
    if(num==ar(num)):
        print(f"{num}: is armstrong number")
    else:
        print(f"{num}: is not armstrong")
num=int(input("enter the number:"))
con(num)

