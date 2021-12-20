def fact(n):
    if (n == 0) | (n == 1):
        return 1
    else:
        return n * fact(n - 1)


n = 4
i = 1
temp_result = 1
while i <= n:
    temp_result = temp_result * fact(i)
    i +=1

print(temp_result)
