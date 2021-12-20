from collections import defaultdict

input = ['Duration', 'F0', 'F1', 'F2', 'F3']
# output = {'Duration': 0, 'F0': 1, 'F1': 2, 'F2': 3, 'F3': 4}

#output = defaultdict()
output = {}
for idx, i in enumerate(input):
    output.update({i: idx})

    print(output)
