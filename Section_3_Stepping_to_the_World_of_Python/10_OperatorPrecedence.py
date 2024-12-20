a = 12  # Not an expression
b = 3   # Not an expression

# a and b are expressions in all these
print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4: integer division, rounded down towards minus infinity
print(a % b)    # 0: the remainder after integer division

print()

print(a + b / 3 - 4 * 12) # -35.0
print(a + (b / 3) - (4 * 12)) # -35.0
print((((a + b) / 3) - 4) * 12) # 12.0
print(((a + b) / 3 - 4) * 12) # 12.0

c = a + b
d = c / 3
e = d - 4
print(e * 12) # 12.0

"""
Operator Precedence Acronyms
    * PEMDAS Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
    * BEDMAS Brackets, Exponents, Division/Multiplication, Addition/Subtraction
    * BODMAS Brackets, Order, Division/Multiplication, Addition/Subtraction
    * Bidmas Backets, Index, Division/Multiplication, Addition/Subraction
"""

print()

print(a / (b * a) / b) # 0.11111111111111

