
def return_list_num():
    print("inside return_list_num")
    return [1 ,2 ,3 ,4 ,5] # pointer returns from the func from method stack to caller

result = return_list_num()

print(result)
for i in result:
    print(i , end=",")

print("\n")
for i in result:
    print(i , end=",")

print("\n test on yield_list_num")
def yield_list_num():
    print("Inside yield_list_num first yield")
    yield 1  # pause and will resume for next call from here saving internal state of the func
    print("Inside yield_list_num sec yield")
    yield 2

result = yield_list_num()

for i in result:
    print("inside loop")
    print(i , end=",")
    print("\n")

# below code will not be executed as iterator is exhausted
for i in result:
    print("inside loop")
    print(i , end=",")

