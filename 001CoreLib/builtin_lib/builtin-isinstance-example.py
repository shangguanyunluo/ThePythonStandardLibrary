class A:
    pass


class B:
    pass


class C(A):
    pass


class D(A, B):
    pass


def dump(object):
    print(object, " => ",)
    if isinstance(object, A):
        print("A")
    if isinstance(object, B):
        print("B")
    if isinstance(object, C):
        print("C")
    if isinstance(object, D):
        print("D")
    print


for i in [A(), B(), C(), D(), 0, "string"]:
    # dump(i)
    pass
print("-" * 20)

def dump2(object):
    print(object, " => ",)
    if issubclass(object, A):
        print("A")
    if issubclass(object, B):
        print("B")
    if issubclass(object, C):
        print("C")
    if issubclass(object, D):
        print("D")
    print


for i in [A, B, C, D, 0, "string"]:
    dump2(i)


