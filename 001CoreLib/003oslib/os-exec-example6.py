import os

program = "python"
arguments = ["hello.py"]
print os.execvp(program, (program,) + tuple(arguments))
print "goodbye"

print("-" * 20)

def run(program, *args):
    pid = os.fork()
    if not pid:
        os.execvp(program, (program,) + args)
    return os.wait()[0]


run("python", "hello.py")
print("goodbye")
