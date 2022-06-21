# 2. Write a program to enter any number and check it is divisible by 7 or not.

while True:
    num = input("Enter any number to check the divisibility by 7 >>> ")
    if not num: break
    num = float(num)
    print(f"Yes, {num} is divisible by 7" if num % 7 == 0 else f"No, {num} is not divisible by 7")