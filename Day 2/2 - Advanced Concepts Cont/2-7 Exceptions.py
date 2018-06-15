import sys

try:
    10 * (1/0)
except ZeroDivisionError as e:
    print 'Divide by zero', e.message, e.args

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()

try:
    try:
        raise NameError('Pig Swill')
    except NameError:
        print 'Lets pass it on'
        raise
except:
    print "Expected error from pass on:", sys.exc_info()[0]
