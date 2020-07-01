'''
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
'''

def rotated_array_search_recursive(input_list, number, start, stop):
    if start == stop:
        return -1
    elif input_list[start] == number:
        return start
    elif input_list[stop] == number:
        return stop

    mid = int((stop - start) / 2) + start

    if input_list[mid] == number:
        return mid

    if input_list[start] > input_list[stop]:
        rotated = True
    else:
        rotated = False

    if rotated:
        if number > input_list[stop]:
            number_left_of_pivot = True
        else:
            number_left_of_pivot = False

        if input_list[start] <= input_list[mid]:
            mid_left_of_pivot = True
        else:
            mid_left_of_pivot = False

    if input_list[mid] < number:
        if not rotated:
            return rotated_array_search_recursive(input_list, number, mid + 1, stop)
        else:
            if number_left_of_pivot == mid_left_of_pivot:
                return rotated_array_search_recursive(input_list, number, mid + 1, stop)
            else:
                return rotated_array_search_recursive(input_list, number, start, mid - 1)
                
    elif input_list[mid] > number:
        if not rotated:
            return rotated_array_search_recursive(input_list, number, start, mid - 1)
        else:
            if number_left_of_pivot == mid_left_of_pivot:
                return rotated_array_search_recursive(input_list, number, start, mid - 1)
            else:
                return rotated_array_search_recursive(input_list, number, mid + 1, stop)

    
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list:
        return -1
    elif len(input_list) == 1:
        if input_list[0] == number:
           return 0
        return -1
    return rotated_array_search_recursive(input_list, number, 0, len(input_list) - 1)


print(rotated_array_search([1], 1))
print(rotated_array_search([2,1], 1))
print(rotated_array_search([2,1], 3))
print(rotated_array_search([2,1], 1))
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 7))
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 8))
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 9))
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 10))
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 2))

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


# Test empty list
print(rotated_array_search([], 1))
# -1


# Test single element list
print(rotated_array_search([1], 1))
# 0

print(rotated_array_search([1], 2))
# -1


# Test rotated with single element
print(rotated_array_search([2,3,4,1], 1))
# 3

print(rotated_array_search([2,3,4,1], 2))
# 0

print(rotated_array_search([2,3,4,1], 3))
# 1

print(rotated_array_search([2,3,4,1], 4))
# 2

print(rotated_array_search([2,3,4,1], 5))
# -1
