import heapq

"""
By default heapq module will re arrange data in min-heap order.
and will provide O(1) access through 

"""
lst = [11, 2, 3, 4, 5, 6]

heapq.heapify(lst)
print(lst)

heap_list = []
heapq.heappush(heap_list,12)
heapq.heappush(heap_list,11)
heapq.heappush(heap_list,1)
heapq.heappush(heap_list,4)
print("After pushing more data into heap")
print(heap_list)

pop_result = heapq.heappop(heap_list)
print(f"pop_result {pop_result}")
pop_result = heapq.heappop(heap_list)
print(f"pop_result {pop_result}")

print("After popping data from heap")
print(heap_list)


