import os
import string


def replace(file, search_for, replace_with):
    # replace strings in a text file
    back = os.path.splitext(file)[0] + ".back"
    tmp = os.path.splitext(file)[0] + ".tmp"

    try:
        os.remove(tmp)
    except os.error:
        pass

    tmp_file = open(tmp, "w")
    with open(file) as f:
        for strings in f.readlines():
            tmp_file.write(strings.replace(search_for, replace_with))
        tmp_file.close()

    try:
        os.remove(back)
    except os.error:
        pass

    os.rename(file, back)
    os.rename(tmp_file.name, file)


replace("hello.py", "again", "world")
