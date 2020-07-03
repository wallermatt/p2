'''
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
'''


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    list_0 = []
    list_1 = []
    list_2 = []
    for e in input_list:
        if e == 0:
            list_0.append(0)
        elif e == 1:
            list_1.append(1)
        elif e == 2:
            list_2.append(2)
    return list_0 + list_1 + list_2


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


# Tests
# 1 element
print(sort_012([0]))
# [0]

# 1 duplicated element
print(sort_012([1,1]))
# [1,1]

# 0,1,2 in list
print(sort_012([1,1,2,0,0,2,2]))
# [0, 0, 1, 1, 2, 2, 2]
