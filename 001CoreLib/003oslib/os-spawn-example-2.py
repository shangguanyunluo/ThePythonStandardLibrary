import os
import string, time


def run(program, *args, **kw):
    mode = kw.get("mode", os.P_WAIT)
    for path in string.split(os.environ["PATH"], os.pathsep):
        file = os.path.join(path, program) + ".exe"
        try:
            return os.spawnv(mode, file, (file,) + args)
        except os.error:
            pass
    raise os.error, "cannot find executable"


run("python", "hello.py", mode=os.P_NOWAIT)
# time.sleep(1)
print("goodbye")
