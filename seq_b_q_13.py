# 13. Write a python program to reverse the given number using while loop.

num = input("Enter the number to be reversed>>> ")
if len(num) == 0: print("Atleast Enter something"); exit()
rev_num = ""
ct = 0

while ct < len(num):
    rev_num += num[len(num)-ct-1]
    ct += 1

if len(num) == 1:
    print("It's the same, don't waste computer's precious processing power by asking stupid questions")
print(rev_num)