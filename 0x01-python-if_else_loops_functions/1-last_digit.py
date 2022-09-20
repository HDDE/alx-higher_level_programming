#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
last_nums = num[-1]
last_num = int(last_nums)
if last_num < 5:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
elif last_num > 6:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
else:
    print(f"Last digit of {number} is {last_num} and is 0")
