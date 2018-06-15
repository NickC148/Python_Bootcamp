# -- simple basic class without methods or members
class Class:
    pass


# -- simple class with class variable i and simple method f


class ClassOne:
    '''A simple example class one'''
    i = 12345

    def f(self):
        return 'Hello my world'


x = ClassOne()
print x.i
# 12345
print x.f()
#['__doc__', '__init__', '__module__', 'data']

# -- class with a constructor __init__ creating a data list instance


class ClassTwo:
    '''A simple example class two'''

    def __init__(self):
        self.data = []


x = ClassTwo()
print dir(x)
x.data.append('fred')
print x.data
# ['fred']

# -- class and instance variables


class Dog:
    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


d = Dog('Fido')
e = Dog('Buddy')
print d.kind, d.name        # shared by all dogs
# canine Fido
print e.kind, e.name        # shared by all dogs
# canine Buddy

# -- Function defined outside the class
# -- Note that this practice usually only serves to confuse the reader of a program.


def f1(self, x, y):
    return min(x, x+y)


class C:
    f = f1

    def g(self):
        return 'hello world'
    h = g


c = C()
print c.h()
# hello world
print c.f(4, 5)
# 4

# -- Methods may call other methods by using method attributes of the self argument:


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


bag = Bag()
bag.add('cow')
print bag.data
# ['cow']
bag.addtwice('moon')
print bag.data
#['cow', 'moon', 'moon']
