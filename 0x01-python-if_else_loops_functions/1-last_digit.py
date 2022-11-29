#!/usr/bin/python3
import random
number = random(-10000, 10000)
if number > 0:
    num = number * -1
    num = num % 5
    num = num * -1
else:
    num = number % 10
    print(f"Last digit of {}".format(number), end=' ')
    if num > 5:
        print(f"is {} and is greater than 5".format(num))
    elif num == 0:
        print(f"is {} is zero".format(num))
    elif num < 6:
        print(f"is {} and is less than 6 and not 0".format(num))
