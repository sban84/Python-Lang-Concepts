from itertools import accumulate
import operator

a_list = [1, 2, 3, 4, 5]

acc = accumulate(a_list)
print(list(acc))

mul = accumulate(a_list, func=operator.mul)
print(mul)

max_item = accumulate(a_list, func=max)
print(max_item)


def accumulate_impl(a: list) -> list:
    temp_sum = a[0]
    result = [temp_sum]
    for idx, i in enumerate(a):
        if idx > 0:
            temp_sum += i
            result.append(temp_sum)

    print(f"result = {result}")
    return result


accumulate_impl(a_list)
