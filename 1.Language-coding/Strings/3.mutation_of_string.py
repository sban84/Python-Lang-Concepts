"""Task
Read a given string, change the character at a given index and then print the modified string.
Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert
Returns

string: the altered string"""


def mutate_string(string, position, character):
    words = string.split(" ")
    result = []
    for w in words:
        print(" inside mutate_string loop " , words)
        updated_word = w[0:position] + character + w[position+1:len(w)]
        result.append(updated_word)
    return result



def prompt_user_input():
    s = input("Enter a string ")
    pos = input("Enter the index you want to change ")
    to_modify = input("Enter the new char(s)  to update ")
    print(f"You have entered {s} , {pos} and {to_modify}")
    result = mutate_string(s,int(pos),to_modify)
    result_str = ""
    result_str = "".join(result)
    print(f"result_str {result_str}")


prompt_user_input()
