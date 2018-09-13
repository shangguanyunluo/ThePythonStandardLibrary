def dump(value):
    print(value, "=>", dir(value))


import sys

dump(0)
dump(1.0)
dump(0.0j)
dump([])
dump({})
dump("string")
dump(len)
dump(sys)

print("-" * 20)


class A:
    def a(self):
        pass

    def b(self):
        pass


class B(A):
    def c(self):
        pass

    def d(self):
        pass


def getmembers(klass, members=None):
    if members is None:
        members = []
    for k in klass.__bases__:
        getmembers(k, members)
    for m in dir(klass):
        if m not in members:
            members.append(m)
    return members

def getmembers2(klass, members=None):
    if members is None:
        members = []
    for k in klass.__bases__:
        getmembers(k, members)
    for m in vars(klass):
        if m not in members:
            members.append(m)
    return members

print(getmembers(A))
print(getmembers(B))
print(getmembers(IOError))

print(getmembers2(A))
print(getmembers2(B))
print(getmembers2(IOError))
print("-"*20)
print vars(A)
print dir(A)

print("-"*20)
book = "library2"
pages = 250
scripts = 350
print "the %(book)s book contains more than %(scripts)s scripts" % vars()
