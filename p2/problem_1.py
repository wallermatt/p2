# problem_1
# Finding the Floored Square Root of an Integer


def sqrt_guess(number, low_guess, high_guess):
    if number == 0:
        return 0
    mid_guess = int((high_guess - low_guess) / 2) + low_guess
    if number // mid_guess == mid_guess:
        return mid_guess
    elif number // mid_guess > mid_guess:
        if number // (mid_guess + 1) < (mid_guess + 1):
            return mid_guess
        return sqrt_guess(number, mid_guess + 1, high_guess)
    elif number // mid_guess < mid_guess:
        return sqrt_guess(number, low_guess, mid_guess - 1)

    
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    return sqrt_guess(number, 1, number)


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

assert sqrt(0) == 0
assert sqrt(1) == 1
assert sqrt(2) == 1
assert sqrt(3) == 1
assert sqrt(4) == 2
assert sqrt(24) == 4
assert sqrt(100000) == 316


print(sqrt(0))
# 0

print(sqrt(1))
# 1

print(sqrt(2))
# 1

print(sqrt(3))
# 1

print(sqrt(100000))
# 316
