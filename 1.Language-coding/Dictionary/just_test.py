def sorted_test(d:dict):
    for k,v in sorted(d.items(), key=lambda kv: kv[1]):
        print(k,v)


d = {}
d.update({"s":2,"a":10})
sorted_test(d)