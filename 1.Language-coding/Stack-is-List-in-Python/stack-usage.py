"""Python’s lists are implemented as dynamic arrays internally, which means they occasionally need to resize the storage space for elements stored in them when elements are added or removed. The list over-allocates its backing storage so that not every push or pop requires resizing. As a result, you get an amortized O(1) time complexity for these operations.

The downside is that when array needs to be recreated for huge items
@TODO check internal of list """

# along with these push and pop , we can get other lists features like access in O(1)
# but not relevant for stack but we can use if required.

stack = []

stack.append(1)  # for adding use append , will add in the end and O(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)

item_deletd = stack.pop()  # use pop for delete from the end  , O(1)
print(f"item deleted {item_deletd} and stack remians with {stack}")





