#
# Example file for working with functions
#
# function with default value for an argument


def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result * num
    return result


print(power(2))
print(power(2,3))
