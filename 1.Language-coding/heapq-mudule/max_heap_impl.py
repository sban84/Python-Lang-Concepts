import heapq

"""
By default heapq module will re arrange data in min-heap order.
and will provide O(1) access through 
So to implement Max Heap we just need to override heappush and heappop of
the original heapq module's API 
"""


class MaxHeap:
    def __init__(self, heap_list):
        self.heap_list = heap_list

    def heappush(self, item):
        heapq.heappush(self.heap_list, -item)

    def heappop(self):
        return -heapq.heappop(self.heap_list)


# testing
heap_list = []
max_heap = MaxHeap(heap_list)
max_heap.heappush(12)
max_heap.heappush(10)
max_heap.heappush(100)
max_heap.heappush(1)

print("after pushing items into Max Heap ", max_heap.heap_list)

print(max_heap.heappop())
print("after popping one items from Max Heap ", max_heap.heap_list)
print(max_heap.heappop())

