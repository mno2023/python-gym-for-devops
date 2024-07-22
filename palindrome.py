#!/usr/bin/python3

def palindrome(st):

    if st == st[::-1]:
        print (f"Given string: \'{st}\' is palindrome")
    else:
        print (f"Given string: \'{st}\' is non-palindrome")


if __name__ == "__main__":

    your_string = input("Please enter your string : ")
    palindrome(your_string)
