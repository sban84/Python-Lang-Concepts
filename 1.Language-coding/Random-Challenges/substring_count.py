"""This is to find out the Counting number of times a substring appears in a string"""


def count_substring_count(s: str, sub: str):
    temp = ""
    counter = 0
    sub_pointer = 0
    for c in s:
        if (sub_pointer < len(s)) and (c == sub[sub_pointer]):
            temp += c
            if temp == sub:
                counter += 1
                sub_pointer = 0
                temp = ""
            else:
                sub_pointer += 1
        else:
            temp = ""
            sub_pointer = 0
    return counter


word_to_lookfor = "el"
word = "helloel"
print(f"{word_to_lookfor} found in the {word} {count_substring_count(word, word_to_lookfor)} times")
