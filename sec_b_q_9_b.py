# 9. Write a Python Program to Calculate the Area of a Triangle.

# Using Heron's Formula (maths brain!!)
s1 = float(input("Enter the length of the side 1 of the triangle >>> "))
s2 = float(input("Enter the length of the side 2 of the triangle >>> "))
s3 = float(input("Enter the length of the side 3 of the triangle >>> "))

s = (s1 + s2 + s3) / 2
area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
print(f"Area of the triangle is {area} units^2")
print("Do it yourself afterwards, even a bio student can do this!")