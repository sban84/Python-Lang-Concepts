

"""File Handling in Python """

with open("./words.txt" , "r") as fileobj:
    #print(fileobj.readlines())
    """If the size of the file is tiny, it is safe to read the whole file contents into memory. If the file is very 
    large it is often better to read line-by-line or by chunks, 
    and process the input in the same loop. To do that:"""
    lines = fileobj.readlines() # list of lines all in one got into memory
    #print(lines)
    for line in lines:
        print(line)

"""An iterable object is returned by open() function while opening a file. This final way
of reading in a file line-by-line includes iterating over a file object in a for loop. 
Doing this we are taking advantage of a built-in Python function that allows us to iterate 
ver the file object implicitly using a for loop in a combination with using the iterable object. 
This approach takes fewer lines of code, which is always the best practice worthy of following."""

L = ["Geeks\n", "for\n", "Geeks\n"]
# Writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()

def read_big_file(fileName):
    outfile = open("./output.txt" , "w")
    lineCount = 0
    with open(fileName, "r") as fileobj:
        for line in fileobj:
            #print(fileobj.read(4))
            #print(line.strip())
            lineCount +=1
            outfile.write(f"Line: {lineCount} {line.strip()}\n")
    outfile.close()




print("****************************")
read_big_file("./myfile.txt")