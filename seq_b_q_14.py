# 14. Write a python program to Check Prime Number or not.

num = int(input("Enter the number to check prime or not >>> "))
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not prime. It is atleast divisible by {i}")
        exit()

print(f"{num} is a Prime number")