
"""
NOTE- Very good exmaple to foramt string in using f""
Remenber this
"""
def convert_binary(n):
    result =[]
    result_str = ""
    while n >0:
        #print(int(n%2))
        #print(n/2)
        result.append(str(n%2))
        n = n//2

    result.reverse()
    result_str = "".join(result)
    return result_str
    #print(result)

convert_binary(8)

def print_diff_format(n):
    print(f"{n:>10} {oct(n):>10} {hex(n).upper():>10} {convert_binary(n):>10}")


print(f"{10.6852:.2f}")


for i in range(1,11):
    print_diff_format(i)
