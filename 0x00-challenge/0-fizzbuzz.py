#!/usr/bin/python3
""" FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return

    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz", end=' ')
        elif (i % 3 == 0):
            print("Fizz", end=' ')
        elif (i % 5 == 0):
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
    print()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./0-fizzbuzz.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        fizzbuzz(number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        sys.exit(1)
