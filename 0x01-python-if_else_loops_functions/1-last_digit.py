#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit2 = abs(number) % 10
if number < 0:
    lastdigit2 = -lastdigit2
print("Last digit of {} is {} and is ".format(number, lastdigit2), end="")
if lastdigit2 > 5:
    print("greater than 5")
elif lastdigit2 == 0:
    print("0")
else:
    print("less than 6 and not 0")
