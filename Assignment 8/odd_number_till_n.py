# WAP to print the  odd numbers till n
def odd(num):
    count=0
    for i in range(1,num+1):
        if(i%2!=0):
            count+=i
    print(count)
num=int(input("enter the number:"))
print(f" sum of  odd number is:{odd(num)}")