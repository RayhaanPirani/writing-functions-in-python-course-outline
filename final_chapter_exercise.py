"""
Context:
This exercise is intended to test your knowledge on the concepts covered in this course. You will develop a class of number operations with your own functions. You will create functions to add, cube and generate exponential powers of 2.

Instructions:
1. Define the constructor (__init__) by specifying an optional parameter k whose default value is 1.
2. Define a function add within the class which takes two variables and returns the sum of them.
3. Define an inline function which returns the cube of the given number.
4. Define the generator TwoExponents which generates a sequence of exponents of the number 2 (like 2, 4, 8, 16, 32, 64, 128, ...). It takes in a parameter called 'maximum' whose default value is 'k'.
"""

# Code:

class NumberOperations:
    ___ __init__(___, ___ = ___):
        ___

    ___ add(___, ___, ___):
        ___ ___ + ___

    cube = ___

    ___ TwoExponents(___):
        current = 0
        while(current < ___):
            ___
            current += 1

# Solution code:

class NumberOperations:
    def __init__(self, k = 1):
        self.k = k

    def add(self, first, second):
        return first + second

    cube = lambda self, n: n*n*n

    def TwoExponents(maximum = self.k):
        current = 0
        while(current < maximum):
            yield 2 ** current
            current += 1