# 9. Write a Python Program to Calculate the Area of a Triangle.

from math import sqrt

# Using Heron's Formula
s1 = int(input("Enter the length of the side 1 of the triangle >>> "))
s2 = int(input("Enter the length of the side 2 of the triangle >>> "))
s3 = int(input("Enter the length of the side 3 of the triangle >>> "))

s = (s1 + s2 + s3) / 2
area = sqrt(s * (s - s1) * (s - s2) * (s - s3))
print(f"Area of the triangle is {area} units^2")