'''
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
'''


def heapify(arr, n, i):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    """
    largest_pos = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    
    if left_child < n and arr[i] < arr[left_child]:
        largest_pos = left_child
        
    if right_child < n and arr[largest_pos] < arr[right_child]:
        largest_pos = right_child
    
    if largest_pos != i:
        largest_value = arr[largest_pos]
        arr[largest_pos] = arr[i]
        arr[i] = largest_value
        heapify(arr, n, largest_pos)


def update_num1_or_num2(num1, num2, num):
    if len(num1) == len(num2):
        num1 += str(num)
    else:
        num2 += str(num)
    return num1, num2
        

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list:
        return input_list

    n = len(input_list)
    if n == 1:
        return input_list

    for i in range(n, -1, -1): 
        heapify(input_list, n, i)
    num1 = ''
    num2 = ''
    for i in range(1, n, 1):
        num1, num2 = update_num1_or_num2(num1, num2, input_list[0])
        input_list = input_list[1:]
        heapify(input_list, n-i, 0)
    num1, num2 = update_num1_or_num2(num1, num2, input_list[0])
    return [int(num1), int(num2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    print(output)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])


# Tests
# Empty list
print(rearrange_digits([]))
# []

# Single entry
print(rearrange_digits([1]))
# [1]

# Two digits
print(rearrange_digits([1,2]))
# [2,1]

# Odd number of digits
print(rearrange_digits([1,2,3]))
# [31,2]

# Even number of digits
print(rearrange_digits([1,2,3,4]))
# [42,31]

# Even number of digits - reverse order
print(rearrange_digits([4,3,2,1]))
# [42,31]

# Larger list with repeating elements
print(rearrange_digits([1,2,2,4,5,9,8,6,7,1,3]))
# [975431, 86221]
