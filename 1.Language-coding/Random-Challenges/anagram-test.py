
with open("./words.txt") as file:
    lines = file.readlines()

line_count = 0

first_word_list = []
sec_word_list = []
for line in lines:
    #print(line)
    line_count +=1
    first_word_list.append(line.split("=")[0].lower().strip())
    sec_word_list.append(line.split("=")[1].strip().replace('\n','').lower())

print(first_word_list)
print(sec_word_list)
# ['Tar ', 'Arc ', 'Elbow ', 'State ', 'Cider ', 'Dusty ', 'Night ', 'Inch ']

def check_anagrame(w1:str,w2):
    w1_sorted = "".join(sorted(w1))
    w2_sorted = "".join(sorted(w2))
    print(w1_sorted,w2_sorted)
    print(w1_sorted == w2_sorted)
    if w1_sorted == w2_sorted:
        print(f"{w1} and {w2} are anagram")
    else:
        print(f"{w1} and {w2} are NOT anagram")


for i in range(0,len(first_word_list)):
    check_anagrame(first_word_list[i],sec_word_list[i])


