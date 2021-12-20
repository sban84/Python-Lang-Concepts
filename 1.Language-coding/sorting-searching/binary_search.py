# [1,2,3,4,5] , 4

def binary_search(elements, value, left, right):
    if left <= right:
        middle = (left + right) // 2

        if elements[middle] == value:
            print(f"Found {value} at index {middle}")
            return middle

        # left half
        if value < elements[middle]:
            return binary_search(elements, value, left, middle - 1)
        elif value > elements[middle]:
            return binary_search(elements, value, middle + 1, right)

    return -1


l = [1, 2, 3, 4, 5]
print(binary_search(l, value=4, left=0, right=len(l) - 1))

sorted_fruits = ['apple', 'banana', 'orange', 'plum']
binary_search(sorted_fruits, 'apple', 0, len(sorted_fruits) - 1)


# using API
import bisect
print(bisect.bisect_left([11,21,3,4],3))