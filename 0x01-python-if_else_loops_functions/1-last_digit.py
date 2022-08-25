#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
length = len(number) - 1
if length > 5:
    print(f" Last digit of {number:d} is {length:d} and is greater than 5")
elif length == 0: 
    print(f" Last digit of {number:d} is {length:d} and is 0")
elif length < 6 and length != 0:
    print(f" Last digit of {number:d} is {length:d} and is less than 6 and not 0")
