import os
import string
import logging

if os.name in ("nt", "dos"):
    exefile = ".exe"
else:
    exefile = ""


def spawn(program, *args):
    try:
        return os.spawnvp(program, (program,) + args)
    except AttributeError:
        pass
    try:
        spawnv = os.spawnv
    except AttributeError:
        pid = os.fork()
        if not pid:
            os.execvp(program, (program,) + args)
            return os.wait()[0]
    else:
        for path in string.split(os.environ["PATH"], os.pathsep):
            file = os.path.join(path, program) + exefile
            try:
                return spawnv(os.P_WAIT, file, (file,) + args)
            except os.error:
                pass
        raise IOError, "cannot find executable"


spawn("python", "hello.py")
print "goodbye"

