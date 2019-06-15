#
# Example file for variables and expressions
#
# Global vs. local variables in functions


def someFunction():
    global f

    f = "def"
    print(f)


someFunction()
print(f)
