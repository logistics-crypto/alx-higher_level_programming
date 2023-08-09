#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
abs_number = abs(number)
last_digit1 = abs_number % 10
last_digit = abs(last_digit1)

output = "Last digit of {}".format(number)
output += " is {}".format(last_digit)
if last_digit < 0:
    last_digit = -last_digit
if last_digit > 5:
    output += " and is greater than 5"
elif last_digit == 0:
    output += " and is 0"
else:
    output += " and is less than 6 and not 0"

print(output)
