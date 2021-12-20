# 1.
def check_pallindrom(word: str) -> bool:
    print(f"word {reversed(word)}")
    if word == "".join(reversed(word)):
        return True
    else:
        return False


print(check_pallindrom("kayak"))


# 2.
def reverse_string(word: str) -> None:
    rev_str = ""
    for i in range(len(word) - 1, -1, -1):
        rev_str += word[i]
    print(rev_str)


print(reverse_string("hello"))


# 3.
# using some concept called tail recursion,
# this is very useful technique we can solve most of the recursion problems.
def reverse_str_recursive(word: str) -> str:
    def reverse_str_inner(word, rev_str, n):
        if n < 0:
            return rev_str
        else:
            rev_str += word[n]
            return reverse_str_inner(word, rev_str, n - 1)

    return reverse_str_inner(word, "", len("hello") - 1)


print(reverse_str_recursive("hello"))


# 4.
# list = [1,2,3,4] , 8
def find_pairs(lst, n):
    result = []
    map = {}
    for idx, i in enumerate(lst):
        map.update({i: idx})
    print(map)
    for i in lst:
        print("sass", n // i)
        if (n % i == 0) and (n // i in map.keys()):
            print("get an divisor")
            idx = map.get(i)
            if idx is not None:
                result.append((idx, (map.get(n / i))))

    print(result)


find_pairs([1, 2, 3, 4], 8)
