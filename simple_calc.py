#!/usr/bin/python3
"""
simple calulator demo
"""


import math

def display():
	print ("First Python Program")

def addition(a, b):
	return a + b

def product(a, b):
	return a * b

def subtraction(a, b):
	return b - a

def division(b, a):
	return b / a


if __name__ == "__main__":
	display()
	a = int(input("Enter your first number : "))
	b = int(input("Enter your second number : "))
	sum = addition(a, b)
	print (f'Sum of given numbers \'{a}\' and \'{b}\' is {sum}')
	
