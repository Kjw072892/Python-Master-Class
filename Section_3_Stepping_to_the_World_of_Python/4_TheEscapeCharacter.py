splitString = "This string has been\nsplit over\nlines"
# \n gives you a new line
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)
# prints: 1 2   3	4	5
# \t adds space between the characters inside a string

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
# Whenever we need to use a quote i.e., double quote inside a double quote, we must use the escape key like on line 12

print("""The pet shop owner said "No, no, \
 'e's uh,...he's resting". """)
# We can use triple quotes to avoid escaping any keys

anotherSplitString = """This string has been \
split over \
several \
lines"""
# The backslash escapes the new line moving everything on to one line

print(anotherSplitString)

anotherSplitString = """This string has been
split over 
several 
lines"""

print(anotherSplitString)
# We can use triple quotes and python will format the string as seen

print("C:\\Users\Kassie\\notes.txt")
# Here because we want to use a backslash within our text, we must escape the backslash I.E '\\'

print(r"C:\Users\Kassie\notes.txt")
# Here we use the letter 'r' in front of our string to denote a raw string


