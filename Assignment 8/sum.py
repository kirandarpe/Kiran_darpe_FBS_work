# wap to print sum of the following terms
#a) 1+2+3+4 till n
#b) 1!+2!+3! till n
#c) 1^1+2^2 till n

#a)
def sum_of_n_number(num):
    count=0
    n=1
    while(n<=num):
            count+=n
            n+=1
    return count
num=int(input("enter the number:"))
print(f"sum of n number is: {sum_of_n_number(num)} ")

#b)
def sum_of_factorial(num):
      fact=1
      count=0
      for i in range (1,num+1):
        fact*=i
        count+=fact
      return count
num=int(input(" enter your number:"))
print(f" sum of factorial is:{sum_of_factorial(num)}")

#c)
def sum_of_self_power(num):
     n=1
     sum=0
     while(n<=num):
          sum+=n**n
          n+=1
     print(sum)
num=int(input("enter the number:"))
s=sum_of_self_power(num)
print(s)
