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

# 1 is an expression and a // b is another expression
# Range is another expression
# variable i in print is another expression
for i in range(1, a // b): # The range must use ints, cannot use floats, so we use integer division
    print(i)

i = 1
print(i)
i = 2
print(i)
i = 3
print(i)
