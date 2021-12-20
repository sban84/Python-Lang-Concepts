"""

"""
import heapq

persons = [
    {"fname": "sban", "lname": "ban", "age": 32.0},
    {"fname": "shyam", "lname": "ban", "age": 36.0},
    {"fname": "rohit", "lname": "ban", "age": 12.0},
    {"fname": "sban", "lname": "ban", "age": 20.0},
    {"fname": "gopi", "lname": "ban", "age": 32.0}
]

for i in persons:
    print(f"fname {i['fname']} and age {i['age']}")

# 1. get nlargest and nsmallest age by using heapq module ( very helpful to implement DS like Heap)

olderst_emp = heapq.nlargest(2, persons, key=lambda kv: kv["age"])
print(olderst_emp)

# same as above by using sorted, remember the way list of dict is sorted

sorted_per = sorted(persons, key=lambda x: x["age"], reverse=True)  # sorting-searching list by key func
print(sorted_per)

# take first 2
print(sorted_per[:2:])

# 2. Another usage is Heap DS ( min heap )

l = [100, 2, 3, 1, 5, 10]
heapq.heapify(l)
print(f"min item {heapq.heappop(l)}")
print(f"min item {heapq.heappop(l)}")  # O(1) always
