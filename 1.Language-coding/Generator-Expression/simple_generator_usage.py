# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


itr_object = my_gen()
print("next(itr_object)" , next(itr_object))

"""
See below since we have already called once by next so we will get remaining  values 
To restart the process we need to create another generator object using something
like itr_obj = my_gen(). check sample_return_usage.py"""
for i in itr_object:
    print(i)