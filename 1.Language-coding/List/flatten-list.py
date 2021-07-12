
"""use this approach can be for any level of flattening."""

l = [[1,2,3], [10,1,10.0] , [12,[100,200]]]

result = []


def flatten_list(l):
    for i in l:
        if isinstance(i,list):
            flatten_list(i)
        else:
            print(i)
            result.append(i)
    return result


print(f"After flattening a nested list {flatten_list(l)}")

# this is for one level so better use above approach can be for any level .
# r = [item for sublist in l for item in sublist]
# print(r)