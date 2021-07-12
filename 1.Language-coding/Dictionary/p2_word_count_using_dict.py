
# practical usage in case of adding new items in map.
import sorting_dict

def word_count():
    line = "this is a line to be parsed and stored in a dict as dict is good"
    l = line.split(" ")
    words_dict = {}
    for w in l:
        if w in words_dict:
            words_dict.update({ w: (words_dict.get(w) + 1)})
        else:
            words_dict.update({w:1})

    return words_dict
    print(words_dict)

result = word_count()


# sort the dict.
sorted_dict_by_key = sorting_dict.sort_by_keys(result)
print(f"sorted_dict_by_key\n {sorted_dict_by_key}")

sorted_dict_by_value = sorting_dict.sort_by_value(result)
print(f"sorted_dict_by_value\n {sorted_dict_by_value}")

sorted_dict_by_value_desc = sorting_dict.sort_by_value_desc(result)
print(f"sorted_dict_by_value_desc\n {sorted_dict_by_value_desc}")