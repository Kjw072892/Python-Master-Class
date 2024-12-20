"""
    Negative Indexing in Strings:

        We can use negative indexing starting at -1 to retrieve the last character in the string
"""
parrot = "Norwegian Blue"

print(parrot[-1]) # e
print(parrot[-14]) # N

print()

print(parrot)
print(parrot[-11])  # w
print(parrot[-10] + "\n" + parrot[-5] + "\n" + parrot[-11] + "\n" + parrot[-8] + "\n" + parrot[-6] + "\n")

print()

print(parrot)
print(parrot[3 - 14]) # w
print(parrot[4 - 14] + "\n" + parrot[9 - 14] + "\n" + parrot[3 - 14] + "\n" + parrot[6 - 14] + "\n" + parrot[8 - 14] +
      "\n")
# Here we can even use an expression to point to a character index within the string

