# 1. Check if element exists in list in Python

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3]
l3 = [1, 2, 31]


# print(set(l1)-set(l3))

# check l2 is in l1 or not
def check_list_in_another_list(l1, l2):
    to_break = False
    for i in l2:
        if i in l1:
            continue
        else:
            return False
    return True


print(check_list_in_another_list(l1, l3))


# 2. Write a program to print all permutations of a given string
def permute(s, answer):
    print(f"s={s}")
    if (len(s) == 0):
        print(answer, end="  ")
        return

    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        print(rest)
        permute(rest, answer + ch)


# Driver Code
answer = ""

#s = input("Enter the string : ")
s = "abc"

print("All possible strings are : ")
permute(s, answer)

print("\n******")



