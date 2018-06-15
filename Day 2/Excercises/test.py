def Foo(x):
    if x == 1:
        return 1
    else:
        return x + Foo(x - 1)


print Foo(4)
