
""" This is a very good example to understand how init.py can help to import python modules
into another file/script outside of the current dir where the source module is placed
 like here we will be using this module in outside of this dir in using_util.py """


import re


def return_len(s):
    return len(s)


def get_encrypted_str(s: str):
    temp = re.sub('[a-z]', '*', s)
    return temp


class Cat:
    def __init__(self):
        self.color = "red"

    def get_cat_color(self):
        return self.color
