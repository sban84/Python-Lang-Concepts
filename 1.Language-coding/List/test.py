list_1 = [34, 54, 67, 89, 11, 43, 94]

print(list_1)
n = 1
result = [list(reversed(list_1[i:i + 3])) for i in range(0, len(list_1), n)]
result = [list_1[i:i + 3] for i in range(0, len(list_1), n)]
print(result)



# list_1.reverse()
# print(list_1)