execfile("hello.py")


def EXECFILE(filename, locals=None, globals=None):
    exec compile(open(filename).read(), filename, "exec") in locals, globals


EXECFILE("hello.py")

print("-" * 20)


def open(filename, mode="rb"):
    import __builtin__
    file = __builtin__.open(filename, mode)
    if file.read(5) not in ("GIF87", "GIF89"): raise IOError, "not a GIF file"
    file.seek(0)
    return file


fp = open("hello.py")
print len(fp.read()), "bytes"

