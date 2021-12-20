def search(keyword, filename):
    print('generator started')
    with open(filename, 'r') as f:
        # Looping through the file line by line
        for line in f:
            if keyword in line:
                # If keyword found, return it
                yield line


# caller

result = search("line", "./directory.txt")
print(type(result))
print(f"result {next(result)}")
print(f"result {next(result)}")
print(f"result {next(result)}")
print(f"result {next(result)}")
print(f"result {next(result)}")
# print(f"result {next(result)}") no rec in generator iterator



