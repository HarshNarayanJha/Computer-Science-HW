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

expression = ""
for i in range(num, 0, -1):
    expression += f"{i}1x" if i > 1 else f"{i}"

if num <= 10:
    print(f"Do it yourself! Can't you do {expression} ?")
else:
    print("Yes, I agree calculating factorials of big numbers on paper is not an easy job even for a math students")