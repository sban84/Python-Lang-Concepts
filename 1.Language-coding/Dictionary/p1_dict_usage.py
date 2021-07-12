
# creation of dict
# way 1.
d1 = {}
d1["a"] =10
print(d1)

# way 2.
phonebook = {
    "bob": 7387,
    "alice": 3719,
    "jack": 7052,
}

# access items
phonebook.get("bob") # prefer this way
# phonebook["bob"]

# add / update new itens , remember this
phonebook.update({"sban" : "1234"})
print(phonebook)

# remove an item , remember pop("key","default") way to delete from dict.
"""NOTE 
Python pop() vs del
First, the pop() method returns the value of the key removed from a dictionary whereas del does 
not return any value. Second, the del keyword returns a KeyError if a key is not in a 
dictionary. On the other hand, the pop() method only returns a KeyError if you do not specify 
a second parameter.
default=None is optional , if we don't pass then keyerrror for non existent passed key. """

deleted_item = phonebook.pop("bob", None)
print(f"deleted_item {deleted_item} and after delete the map is {phonebook}")

# del phonebook["sban"]
# print(phonebook)

phonebook.update({"sban": 100}) # insert / update both refer this
#phonebook.update([("rohit",200)])
print("after adding new items in dict " , phonebook)










