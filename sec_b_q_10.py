# 10. Python Program to Find the Factorial of a Number.

def factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        fact *= i

    return fact

num = int(input("Input a number to find the factorial of >>> "))
if num < 0:
    raise ValueError("Factorial of negatives is not defined")

if num == 0:
    print(f"{num}! = 1")
else:
    print(f"{num}! = {factorial(num)}")