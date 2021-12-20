from collections import deque




lst = [1, 2, 3, 4, 5]
d = deque(lst)
print(d)

d.rotate(3) # -ve for left rotate
print(d)


# way 2 , using list
# i/p -> 1,2,3,4,5 , 3
# o/p -> 3,4,5,1,2
def right_rotate(lst: list, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]


result = right_rotate([1, 2, 3, 4, 5], 3)
print(result)


def left_rotate(lst, n):
    n = n % len(lst)
    return lst[n:] + lst[:n]

print(f"left rorate result {left_rotate([1, 2, 3, 4, 5,6], 2)}")
