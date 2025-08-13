# WAP to check the number is  armstrong or n

num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)
sum_of_powers = 0

for digit in num_str:
    sum_of_powers += int(digit) ** num_digits

if num == sum_of_powers:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
