#WAP to print sum of prime number using function
def prime(num):
    count=0
    for j in range(2,num+1):
        i=2
        while(i<j):
            if(j%i==0):
                break
            i+=1
        else:
            count+=j
    return count
    
# input the function
num=int(input("enter the number:"))
# call the function
sum=prime(num)
print(f"sum of prime number is:{sum}")