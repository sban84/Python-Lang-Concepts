def merge_sort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[0:mid]
        right = myList[mid:len(myList)]
        merge_sort(left)
        merge_sort(right)

        # This part will come after the recursion finished ,
        # Three iterators for traversing the two halves and k for result
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):  # this while loop is must
            if left[i] <= right[j]:
                myList[k] = left[i]  # inplace
                result[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                result[k] = right[j]
                j += 1

            # Move to the next slot
            k += 1

        # do for the left over items
        while i < len(left):
            myList[k] = left[i]
            result[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            myList[k] = right[j]
            result[k] = right[j]
            j += 1
            k += 1



l = [54, 26, 93, 17, 77, 31, 44, 55, 20]
result = l.copy()  # if we wanted to store sorted result into another list
merge_sort(l)
print(f"After sorting using Merge Sort Algorithm {l}")
print(f"After sorting using Merge Sort Algorithm {result}")
