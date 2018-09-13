def dump(value):
    print(type(value), "=>", value)


dump(0)
dump(1.0)
dump("one")

print("-" * 20)


def load(file):
    print file, "==="
    if isinstance(file, type("")):
        file = open(file, "r")
    return file.read()


print(len(load("hello.py")))
print(len(load(open("hello.py", "rb"))))
print(len(load("example-plugin.py")))

print("-" * 20)


def dump(function):
    if callable(function):
        print function, "is callable."
    else:
        print function, "is not callable."


class A:
    def method(self, value):
        return value


class B:
    def __call__(self, value):
        return value


a = A()
b = B()

dump(0)
dump("string")
dump(callable)
dump(dump)

dump(A)
dump(B)
dump(A.method)

dump(a)
dump(b)
dump(a.method)
