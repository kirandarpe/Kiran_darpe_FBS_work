# Prime numbers till n
num=int(input("enter the number:"))
for j in range(2,num+1):
    is_prime = True
    for i in range(2, int(j ** 0.5) + 1):
        if j % i == 0:
            is_prime = False
            break
    if is_prime:
        print(j, end=" ")

