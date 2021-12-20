import os

# Use shutil for copy files and move operations
from shutil import move, copy2


def rsplit_test():
    file_name = "abc_file_txt"

    try:
        ext = file_name.rsplit(".", 1)[1]
        print(f"ext {ext}")
    except IndexError as err:
        print("extension not found")


def file_search(root_dir: str):
    result = ""
    found_dict = {i: [] for i in ["txt", "py"]}
    for (dirPath, dirName, files) in os.walk(root_dir):
        # print("dirPath", dirPath)
        # print("dirName", dirName)
        # print("file",files)
        for file in files:
            ext = file.rsplit(".")[1]
            if ext in ["txt", "py"]:
                result += f"File Found {file} \n"
                found_dict.get(ext).append(os.path.join(dirPath, file))

    print("found_dict" , found_dict)
    return result


result = file_search(".")

