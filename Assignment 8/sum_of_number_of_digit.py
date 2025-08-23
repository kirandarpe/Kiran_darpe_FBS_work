# write a program to print sum of number of digit
def sum_dig(num):
    d=0
    while(num>0):
        d+=num%10
        num//=10
    return d
num=int(input("enter the number:"))
sum=sum_dig(num)
print(sum)
