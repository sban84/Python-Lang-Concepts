""" this is very good to remember
Soring of dic in Python"""


# -> dict is optional
def sort_by_keys(d: dict):
    """
    :rtype: object
    """
    print("Sorting by key ")
    sorted_dict = {}
    # for k, v in sorted(d.items()):
    for k, v in sorted(d.items(), key=lambda kv: kv[0]):
        # print(f"key = {k} and value= {d.get(k)}")
        sorted_dict.update({k: d.get(k)})
    return sorted_dict


def sort_by_value(d: dict):
    # print("Sorting by value ")
    sorted_dict = {}
    for k, v in sorted(d.items(), key=lambda kv: kv[1]):
        # print(f"key = {k} and value= {d.get(k)}")
        sorted_dict.update({k: d.get(k)})
    return sorted_dict


def sort_by_value_desc(d):
    sorted_dict = {}
    print("***Sorting by value in descending order*** ")
    for k, v in sorted(d.items(), key=lambda kv: kv[1], reverse=True):
        sorted_dict.update({k: d.get(k)})
    return sorted_dict
