"""collections.deque: Fast and Robust Stacks
The deque class implements a double-ended queue that supports adding and removing elements from either end in O(1) time
(non-amortized). Because deques support adding and removing elements from either end equally well, they can serve both as queues and as stacks.

Python’s deque objects are implemented as doubly-linked lists, which gives them excellent and consistent performance for
inserting and deleting elements but poor O(n) performance for randomly accessing elements in the middle of a stack.

Overall, collections.deque is a great choice if you’re looking for a stack data structure in Python’s standard library
that has the performance characteristics of a linked-list implementation:
Since like stack , queue DS need push and pop but its FIFO order
so if we use list for that then after pop we need shuffle everytime ,
So python provides seperate DS for that its called collections.deque
"""

from collections import deque

queue = deque()
queue.appendleft(1)
queue.appendleft(2)
queue.appendleft(3)



print(queue)

item_deleted = queue.pop()
print(item_deleted)



