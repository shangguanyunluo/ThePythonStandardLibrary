import os

os.mkdir("test")
os.rmdir("test")
# os.rmdir("samples")

print("-" * 20)

file = "bird.jpg"

import time


def dump(st):
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    print "- size:", size, "bytes"
    print "- owner:", uid, gid
    print "- created:", time.ctime(ctime)
    print "- last accessed:", time.ctime(atime)
    print "- last modified:", time.ctime(mtime)
    print "- mode:", oct(mode)
    print "- inode/dev:", ino, dev


st = os.stat(file)
print "stat", file
dump(st)

print

fp = open(file)
st = os.fstat(fp.fileno())
print("fstat", file)
dump(st)
