a_list = [(1, 2), (5, 1), (3, -1), (100, 200)]

a_list_sorted_by_pair_sum = sorted(a_list, key=lambda x: x[0]+x[1], reverse=False)
print(f"a_list_sorted_by_pair_sum {a_list_sorted_by_pair_sum}")