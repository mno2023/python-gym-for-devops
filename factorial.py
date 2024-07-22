#!/usr/bin/python3

"""
Computes the factorial of a given number.

"""

num = int(input("Enter your number : "))
result = 1
if num <= 0:
    print ("Please enter a positive value greater than ZERO.")

for item in range(1, num + 1):
    result *= item

print (f"Factorial of given : {num} is {result}.")

