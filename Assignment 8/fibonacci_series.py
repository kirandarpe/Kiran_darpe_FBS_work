#WAP to print fibonacci series
def fibonacci(num):

    a=0
    b=1
    for i in range(1,num+1):
        print(a,end=" ")
        c=a+b
        a=b
        b=c

num=int(input("enter the number:"))
fibonacci(num)