'''
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
'''

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return False

    min = ints[0]
    max = ints[0]

    for value in ints:
        if value < min:
            min = value
        if value > max:
            max = value

    return (min,max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# Tests
ints = []
print(get_min_max(ints) == False)
# True

ints = [1]
print(get_min_max(ints) == (1,1))
# True

ints = [1,2,3,5]
print(get_min_max(ints) == (1,5))
# True

ints = [5,4,3,2,1]
print(get_min_max(ints) == (1,5))
# True
