#a
n = int(input("Enter n: "))
fact = 1
sum_fact = 0
for i in range(1, n+1):
    fact *= i
    sum_fact += fact
print("Sum of factorial series =", sum_fact)
#b
N = int(input("Enter N: "))
sum_power = 0
for i in range(1, N+1):
    sum_power += N ** i
print("Sum of powers =", sum_power)
#c
n = int(input("Enter n: "))
a = 1
r = 2
sum_gp = a * (r**n - 1) // (r - 1)
print("Sum of GP =", sum_gp)

#d
n = int(input("Enter n: "))
a = 1
r = 2
sum_gp = a * (r**n - 1) // (r - 1)
print("Sum of GP =", sum_gp)
#e
n = int(input("Enter n: "))
a = 1
r = 2
sum_gp = a * (r**n - 1) // (r - 1)
print("Sum of GP =", sum_gp)

