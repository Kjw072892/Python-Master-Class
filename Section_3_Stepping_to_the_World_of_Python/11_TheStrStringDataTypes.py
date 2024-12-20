
"""
    Programming languages starts with the number 0 instead of 1. So index 3 in parrot is w.
"""

"""
    Mini Challenge:
        Add some code to the program, so that it prints out we win.
        
        Each character should appear on a separate line.
        
        The program should get the characters from the parrot string, using indexing.
        
        The w is already printed out, you just need to print the remaining 5 characters.
        
        With the text that is already being printed, the final output from the program should be:
        
        Norwegian Blue
        w
        e
        
        w
        i
        n
"""
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3]) # w

print(parrot[4] + "\n" + parrot[9] + "\n" + parrot[3] + "\n" + parrot[6] + "\n" + parrot[8] + "\n")