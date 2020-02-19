"""
# with type int
print("With Float")
# Addition
print(2 + 3)
# Subtraction
print(3 - 2)
# Multiplication
print(2 * 3)
# Division
print(2 / 3)

print("\nWith Float")
# with Float
# Addition
print(2.2 + 3.3)
# Subtraction
print(3.3 - 2.2)
# Multiplication
print(2.2 * 3.3)
# Division
print(2.2 / 3.3)

# with type complex
print("\nComplex ")
# Addition
print((2 + 3j) + (1 + 2j))
# Subtraction
print((3 - 2j) - (2 - 1j))
# Multiplication
print((2 * 3j) * (1 * 2j))
# Division
print((2 / 3j) / (1 / 2j))

print("\nPower")
print(2 ** 3)

print("\nFull Division - round off quotient")
print(2 // 3)

print("\nModulus - In computing, the modulo operation finds the remainder after division of one number by another")
print(2 % 3)
"""

"""
https://docs.python.org/3/library/math.html
"""
print("\nMath Functions ")


print("\nRound")
print(round(3.4))  # < .5
print(round(3.5))  # >= .5

print("\nAbsolute Value")
print(abs(-10))
print(abs(10))

'''
math.ceil(x)
Return the ceiling of x, the smallest integer greater than or equal to x. 
If x is not a float, delegates to x.__ceil__(), which should return an Integral value.
'''
import math as m

print("\nceil ")
print(m.ceil(5.4)) # .1 t0 .9 is rounded to its value or 5.1 to 5.9 is equal to 5

'''
math.factorial(x)
Return x factorial as an integer. Raises ValueError if x is not integral or is negative.
'''

print("\nFactorial")
print(m.factorial(5))
print(5*4*3*2*1) # factorial
'''
Factorial of 5 is 
5 x 4 x 3 x 2 x 1
'''

'''
 math.gcd(a, b)
Return the greatest common divisor of the integers a and b. If either a or b is nonzero, 
then the value of gcd(a, b) is the largest positive integer that divides both a and b. gcd(0, 0) returns 0.
'''

print("\nGCD")
print(m.gcd(4,2))


'''There are so many inbuilt math functions in python where we will use few and refer python documentation to learn 
whichever is necessary. '''