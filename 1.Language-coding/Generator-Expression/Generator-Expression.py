

def rev_str(s):
    print("Inside rev_str generator function")
    for i in range( len(s) -1 ,-1,-1 ):
        print("Generator will pause and resume")
        yield s[i] # will maintain the state and local values and pause for the next successive call.


s = "hello"

gen_iterator_obj = rev_str(s)
print(gen_iterator_obj)
for i in gen_iterator_obj: # this will invoke generator, by calling this generator will return one char one by one.
    print("Calling itr instance one by one ")
    print(i , sep=" ")

